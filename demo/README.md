# TP4 Grupo 5 - Demo de observabilidad

Prometheus + Grafana + node_exporter + blackbox_exporter + nginx de prueba.

## Levantar
```
docker compose up -d --build
```
- Grafana: http://localhost:3000 (admin / admin) -> dashboard "TP4 Grupo 5 - Observabilidad"
- Prometheus: http://localhost:9090 (targets en /targets, alertas en /alerts)
- Nginx de prueba: http://localhost:8080

## Probar la alerta
```
docker stop nginx     # tras ~30 s la alerta ServicioCaido pasa a Firing
docker start nginx    # vuelve a OK
```

## Bajar todo
```
docker compose down
```

## Sin internet
Con conexión: `docker compose up -d --build` (la primera vez construye `notifier`). Después todo funciona offline, salvo el envío final a ntfy (necesita internet).

## Notificaciones (ntfy)
Flujo: Prometheus -> Alertmanager -> webhook -> MQTT (mosquitto) -> ntfy.sh

Suscribirse al topic `utnfrlp-g5-alertas-7f3k` desde la app de ntfy o en https://ntfy.sh/utnfrlp-g5-alertas-7f3k
(cualquiera que conozca el nombre del topic puede leerlo).

Ver qué pasa por MQTT: `docker exec mosquitto mosquitto_sub -t alertas/prometheus`
Logs del puente: `docker logs -f notifier`
