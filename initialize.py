import os

carpetas = [
    os.path.join("data", "raw"),
    os.path.join("data", "silver"),
    os.path.join("data", "gold"),
    "reports"
]

for carpeta in carpetas:
    os.makedirs(carpeta, exist_ok=True)

print("=" * 60)
print("INITIALIZE - CIPSA CIPTECH")
print("=" * 60)
print("Estructura de directorios verificada y creada correctamente.")