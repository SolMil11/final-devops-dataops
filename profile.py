import csv
import os

archivo = os.path.join("data", "raw", "ordenes_compra_2025.csv")

if os.path.exists(archivo):
    with open(archivo, encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        total_filas = len(reader)
        columnas = list(reader[0].keys()) if total_filas > 0 else []

    print("=" * 60)
    print("PROFILE (CAPA RAW) - CIPSA CIPTECH")
    print("=" * 60)
    print(f"Total de registros analizados: {total_filas}")
    print(f"Columnas detectadas: {columnas}")
else:
    print("Error: No se encontro el archivo de datos raw.")