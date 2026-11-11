# TP4 Grupo 5 - Demo de observabilidad

Prometheus + Grafana + node_exporter + blackbox_exporter + nginx de prueba.

## Levantar
```
docker compose up -d
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
Con conexión: `docker compose pull`. Después ya funciona offline.
