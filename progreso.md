# Bitácora del grupo — TP4

> Registrar acá el avance: qué hizo cada integrante, decisiones tomadas y pendientes.
> Esto ayuda a coordinar el trabajo y deja evidencia de la participación de todos.

---

## 👥 Integrantes

| Nombre | Usuario de GitHub | Rol en el grupo |
|--------|-------------------|-----------------|
| Vidmar, Ian | IGVR1 | [completar] |
| Atencio, Juan | juann-ign | [completar] |
| Borda, Patricio | Patricioborda | [completar] |

## 🎯 Proyecto

- **Modalidad:** B — Artículo de Revisión del Estado del Arte
- **Tema:** Del SNMP a la observabilidad moderna: estado del arte del monitoreo de redes con Prometheus y Grafana
- **Problema/objetivo:** Analizar cómo evolucionó el monitoreo de redes (SNMP, Syslog, NetFlow/IPFIX, Prometheus con exporters, streaming telemetry con gNMI), qué innovaciones están cambiando el panorama (OpenTelemetry, eBPF, Hubble, detección de anomalías) y qué problemas siguen abiertos (cardinalidad, escalado, correlación de métricas/logs/trazas).

### Integración de las 3 áreas

- **Redes:** qué se mide en una red (interfaces, errores, latencia, disponibilidad) y cómo se obtiene (polling, push, flujos, telemetría).
- **Operación:** monitoreo, alertas y dashboards como código; comparación entre enfoques y herramientas.
- **Seguridad:** el monitoreo como herramienta de detección (anomalías de tráfico, caídas sospechosas) y la seguridad del propio stack de monitoreo (SNMPv3 vs v2c, TLS y autenticación, exposición de exporters).

### Plan de entregables

- **Documento:** estructura del template B (Resumen, Introducción, Estado del arte con tabla comparativa de enfoques de monitoreo, Innovaciones emergentes, Oportunidades y desafíos, Conclusiones, Referencias con mínimo 6: paper académico, documentación oficial de Prometheus/Grafana y RFC de SNMP/IPFIX/Network Telemetry, entre otras).
- **Demo / estación:** demo reproducible con docker compose (Prometheus, Grafana, node_exporter y blackbox_exporter), offline en la laptop. Muestra métricas reales de la máquina y de servicios locales, y una alerta que se dispara cuando un servicio cae. Dura 3-5 minutos, con plan B grabado.
- **Póster:** A1, con diagrama de arquitectura de la solución de monitoreo (o línea de tiempo de la evolución), tabla comparativa resumida, capturas del dashboard de la demo, conclusiones y QR al repositorio.

## 🗓️ Registro de avance

| Fecha | Qué se hizo | Quién | Commit |
|-------|-------------|-------|--------|
| 06/11/2026 | Se definió modalidad B y el tema; se envió la propuesta a los profesores para su aprobación | Ian Vidmar (envío), grupo | |

## 🚧 Pendientes / decisiones

- [x] Definir tema definitivo (pendiente de aprobación de la cátedra)
- [x] Elegir modalidad (B — Estado del Arte)
- [ ] Asignar roles (quién escribe el documento, quién arma la demo, quién el póster)
- [ ] Esperar la respuesta de los profesores a la propuesta
- [ ] Confirmar con la cátedra las fechas vigentes de entrega y de la Feria de Redes
- [ ] Completar usuarios de GitHub y agregar a los docentes como colaboradores
- [ ] Seleccionar las referencias (mínimo 6: paper, documentación oficial y RFC)

## 📝 Notas

- Propuesta enviada a los profesores con dos consultas abiertas:
  1. En la modalidad B, ¿la demo debe ser una estación funcionando como la planteada, o alcanza con otro formato (por ejemplo, la presentación)?
  2. El README del póster pide diagrama de la solución (topología de red) y resultados. Como en B no se implementa una red, ¿está bien reemplazarlos por los hallazgos de la revisión más las capturas de la demo?
- Hasta tener respuesta, avanzar con el documento y la demo según lo propuesto.