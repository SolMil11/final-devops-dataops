import csv
import os

entrada = os.path.join("data", "silver", "ordenes_enriquecidas.csv")
salida = os.path.join("data", "gold", "reporte_ordenes_compra_final.csv")

datos = []
with open(entrada, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    datos = list(reader)

with open(salida, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(datos)

print("=" * 60)
print("PUBLISH (CAPA GOLD) - CIPSA CIPTECH")
print("=" * 60)
print(f"Datos consolidados correctamente en la Capa Gold: {salida}")