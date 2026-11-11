"""Alertmanager --webhook--> MQTT (mosquitto) --> ntfy.sh

1) Recibe el webhook de Alertmanager y publica cada alerta en MQTT.
2) Se suscribe al mismo topico MQTT y manda cada alerta a ntfy.
"""
import json
import os
import urllib.request
from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer

import paho.mqtt.client as mqtt

MQTT_HOST = os.getenv("MQTT_HOST", "mosquitto")
MQTT_TOPIC = "alertas/prometheus"
NTFY_URL = os.getenv("NTFY_URL", "https://ntfy.sh") + "/" + os.getenv("NTFY_TOPIC", "utnfrlp-g5-alertas-7f3k")
AR = timezone(timedelta(hours=-3))


def hora(iso):
    dt = datetime.strptime(iso[:19], "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc)
    return dt.astimezone(AR).strftime("%d/%m/%Y %H:%M:%S")


def armar_mensaje(a):
    """Devuelve (titulo, cuerpo, prioridad, tags) para ntfy."""
    labels, notas = a.get("labels", {}), a.get("annotations", {})
    firing = a.get("status") == "firing"
    nombre = labels.get("alertname", "alerta")
    lineas = [
        f"Servicio: {labels.get('instance', '?')}",
        f"Severidad: {labels.get('severity', '?')}",
        f"Detalle: {notas.get('summary', '-')}",
        f"Desde: {hora(a['startsAt'])} (hora AR)",
    ]
    if firing:
        return f"ALERTA: {nombre}", "\n".join(lineas), "urgent", "rotating_light"
    lineas.append(f"Recuperado: {hora(a['endsAt'])} (hora AR)")
    return f"RESUELTA: {nombre}", "\n".join(lineas), "default", "white_check_mark"


# ---- MQTT -> ntfy ----
def on_connect(client, userdata, flags, reason_code, properties):
    print("MQTT conectado, suscripto a", MQTT_TOPIC, flush=True)
    client.subscribe(MQTT_TOPIC)


def on_message(client, userdata, msg):
    try:
        titulo, cuerpo, prio, tags = armar_mensaje(json.loads(msg.payload))
        req = urllib.request.Request(
            NTFY_URL, data=cuerpo.encode("utf-8"),
            headers={"Title": titulo, "Priority": prio, "Tags": tags},
        )
        urllib.request.urlopen(req, timeout=10)
        print("ntfy OK:", titulo, flush=True)
    except Exception as e:  # sin internet no debe romper el puente
        print("ntfy FALLO:", e, flush=True)


mq = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mq.on_connect, mq.on_message = on_connect, on_message
mq.connect_async(MQTT_HOST, 1883)
mq.loop_start()


# ---- Alertmanager -> MQTT ----
class Webhook(BaseHTTPRequestHandler):
    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        for alerta in data.get("alerts", []):
            mq.publish(MQTT_TOPIC, json.dumps(alerta))
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args):
        pass


HTTPServer(("0.0.0.0", 8000), Webhook).serve_forever()
