import csv
import os

archivo = os.path.join("data", "raw", "ordenes_compra_2025.csv")
errores = 0

with open(archivo, encoding="utf-8") as f:
    for i, row in enumerate(csv.DictReader(f), start=1):
        if not row["id_orden"] or not row["proveedor"] or not row["gestor"]:
            print(f"Fila {i}: Error por campos vacios.")
            errores += 1
        try:
            float(row["monto_ejecutado"])
            float(row["monto_presupuestado"])
        except ValueError:
            print(f"Fila {i}: Error en formato numerico de montos.")
            errores += 1

print("=" * 60)
print("QUALITY GATE - CIPSA CIPTECH")
print("=" * 60)
if errores == 0:
    print("Control de Calidad APROBADO: 0 errores detectados.")
else:
    print(f"Control de Calidad FALLIDO: {errores} errores detectados.")