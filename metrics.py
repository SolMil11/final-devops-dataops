import csv
import os

entrada = os.path.join("data", "silver", "ordenes_enriquecidas.csv")
reporte = os.path.join("reports", "resumen_ejecucion.txt")

total_monto_ejecutado = 0.0
total_monto_presupuestado = 0.0
gestores_conteo = {}

with open(entrada, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        ejecutado = float(row["monto_ejecutado"])
        presupuestado = float(row["monto_presupuestado"])
        gestor = row["gestor"]

        total_monto_ejecutado += ejecutado
        total_monto_presupuestado += presupuestado
        gestores_conteo[gestor] = gestores_conteo.get(gestor, 0) + 1

resumen = f"""
============================================================
METRICAS DE LOGISTICA Y COMPRAS - CIPSA CIPTECH 2025
============================================================
Total Presupuestado : S/ {total_monto_presupuestado:,.2f}
Total Ejecutado     : S/ {total_monto_ejecutado:,.2f}
Variacion Total     : S/ {(total_monto_ejecutado - total_monto_presupuestado):,.2f}

Distribucion por Gestor:
"""
for gestor, cantidad in gestores_conteo.items():
    resumen += f"- {gestor}: {cantidad} ordenes de compra\n"

with open(reporte, "w", encoding="utf-8") as f:
    f.write(resumen)

print(resumen)
print(f"Reporte de metricas generado en: {reporte}")