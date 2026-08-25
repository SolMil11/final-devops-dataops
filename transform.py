import csv
import os

os.makedirs("data/silver", exist_ok=True)

entrada = os.path.join("data", "raw", "ordenes_compra_2025.csv")
salida = os.path.join("data", "silver", "ordenes_enriquecidas.csv")
resultado = []

with open(entrada, encoding="utf-8") as f:
    for row in csv.DictReader(f):
        ejecutado = float(row["monto_ejecutado"])
        presupuestado = float(row["monto_presupuestado"])
        
        # Calcular la diferencia (Ejecutado vs Presupuestado)
        diferencia = round(ejecutado - presupuestado, 2)
        
        # Regla de negocio logistica
        if ejecutado > presupuestado:
            estado_presupuesto = "SOBREPRESUPUESTO"
        elif ejecutado == presupuestado:
            estado_presupuesto = "EXACTO"
        else:
            estado_presupuesto = "AHORRO"

        row["diferencia_monto"] = diferencia
        row["estado_presupuesto"] = estado_presupuesto
        resultado.append(row)

# Definimos las cabeceras incluyendo los nuevos campos calculados
fieldnames = list(resultado[0].keys())

with open(salida, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(resultado)

print("=" * 60)
print("TRANSFORM (CAPA SILVER) - CIPSA CIPTECH")
print("=" * 60)
print(f"Total de ordenes transformadas: {len(resultado)}")
print(f"Archivo generado: {salida}")