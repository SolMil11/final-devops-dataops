import csv
import os
from datetime import datetime

os.makedirs("data/raw", exist_ok=True)

# 50 Ordenes de compra a proveedores - CIPTECH (CIPSA) 2025 con 2 gestores
datos_ordenes = [
    ["OC-8001", "Plasticos Industriales S.A.", "Materia Prima (Polimeros)", "45000", "42000", "2025-11-10", "Soledad Garate"],
    ["OC-8002", "TecnoMoldes Peru EIRL", "Moldes de Inyeccion", "28000", "30000", "2025-11-12", "Joel Lopez"],
    ["OC-8003", "Global Logistics S.A.C.", "Servicio de Transportes", "12500", "12500", "2025-11-15", "Soledad Garate"],
    ["OC-8004", "Insumos Quimicos del Sur", "Aditivos y Colorantes", "18500", "19000", "2025-11-18", "Joel Lopez"],
    ["OC-8005", "ElectroIndustrial Tech", "Mantenimiento de Maquinaria", "9200", "10000", "2025-11-20", "Soledad Garate"],
    ["OC-8006", "Sistemas y Redes Corporativas", "Licencias de Software Jira", "15000", "15000", "2025-11-22", "Joel Lopez"],
    ["OC-8007", "Envases y Embalajes del Peru", "Cajas de Carton Corrugado", "8400", "8000", "2025-11-25", "Soledad Garate"],
    ["OC-8008", "Metalurgica CIPSA Proveedores", "Piezas Metalicas de Repuesto", "22000", "21000", "2025-11-28", "Joel Lopez"],
    ["OC-8009", "Servicios Generales Limpieza", "Limpieza Industrial Planta", "6500", "6500", "2025-12-01", "Soledad Garate"],
    ["OC-8010", "Lubricantes y Derivados S.A.", "Aceites para Motores de Extrusion", "11000", "12000", "2025-12-03", "Joel Lopez"],
    ["OC-8011", "Equipos de Seguridad EPP S.A.C.", "Implementos de Seguridad Industrial", "14200", "14000", "2025-12-05", "Soledad Garate"],
    ["OC-8012", "Automatizacion y Control SAC", "Sensores para Lineas CIPTECH", "31000", "29000", "2025-12-08", "Joel Lopez"],
    ["OC-8013", "Hidraulica y Neumatica EIRL", "Valvulas y Conexiones", "17500", "18000", "2025-12-10", "Soledad Garate"],
    ["OC-8014", "Filtros Industriales del Peru", "Filtros de Aire y Agua", "7800", "7500", "2025-12-12", "Joel Lopez"],
    ["OC-8015", "Consultores TI Integrales", "Soporte Infraestructura Redes", "19500", "20000", "2025-12-15", "Soledad Garate"],
    ["OC-8016", "Comercializadora de Aceros", "Perfiles de Acero Inoxidable", "35000", "35000", "2025-12-18", "Joel Lopez"],
    ["OC-8017", "Servicios de Impresion Grafica", "Etiquetas de Identificacion", "5200", "5000", "2025-12-20", "Soledad Garate"],
    ["OC-8018", "Energia y Potencia S.A.", "Mantenimiento Tableros Electricos", "16000", "15500", "2025-12-22", "Joel Lopez"],
    ["OC-8019", "Transportes y Carga pesada", "Logistica de Distribucion Local", "13500", "14000", "2025-12-24", "Soledad Garate"],
    ["OC-8020", "Soluciones Cloud & Data EIRL", "Hosting Servidores y Backup", "24000", "24000", "2025-12-28", "Joel Lopez"],
    ["OC-8021", "Ferreteria Industrial del Centro", "Herramientas de Corte", "4100", "4500", "2025-10-02", "Soledad Garate"],
    ["OC-8022", "Quimica Industrial del Norte", "Disolventes Industriales", "16200", "15000", "2025-10-05", "Joel Lopez"],
    ["OC-8023", "Redes y Cableado Estructurado", "Fibra Optica para Planta", "23000", "22000", "2025-10-08", "Soledad Garate"],
    ["OC-8024", "Válvulas y Bridas del Sur", "Accesorios de Tuberias", "9800", "10000", "2025-10-11", "Joel Lopez"],
    ["OC-8025", "Seguridad Electronica Total", "Cámaras de Videovigilancia", "14500", "14000", "2025-10-14", "Soledad Garate"],
    ["OC-8026", "Motores y Reductores S.A.C.", "Reductores de Velocidad", "29500", "30000", "2025-10-17", "Joel Lopez"],
    ["OC-8027", "Suministros de Oficina y Papel", "Papeleria y Toners", "3200", "3000", "2025-10-20", "Soledad Garate"],
    ["OC-8028", "Compresores y Aire S.A.", "Mantenimiento Compresores", "12100", "12000", "2025-10-23", "Joel Lopez"],
    ["OC-8029", "Iluminacion LED Industrial", "Lámparas para Naves", "8900", "9000", "2025-10-26", "Soledad Garate"],
    ["OC-8030", "Servicios Ambientales Peru", "Gestion de Residuos Solidos", "7500", "7500", "2025-10-29", "Joel Lopez"],
    ["OC-8031", "Plasticos Especiales del Peru", "Masterbatch y Aditivos", "34000", "32000", "2025-09-03", "Soledad Garate"],
    ["OC-8032", "Informatica y Servidores SAC", "Discos Duros NVMe Servidores", "11500", "12000", "2025-09-06", "Joel Lopez"],
    ["OC-8033", "Logistica Portuaria Nacional", "Derechos de Aduana y Puerto", "18200", "18000", "2025-09-09", "Soledad Garate"],
    ["OC-8034", "Cintas y Empaques Industriales", "Cintas de Embalaje", "4900", "5000", "2025-09-12", "Joel Lopez"],
    ["OC-8035", "Mecánica de Precision EIRL", "Torneado de Piezas", "13800", "13500", "2025-09-15", "Soledad Garate"],
    ["OC-8036", "Automatica Industrial Lab", "Plc y Pantallas HMI", "39000", "38000", "2025-09-18", "Joel Lopez"],
    ["OC-8037", "Pinturas y Revestimientos S.A.", "Pintura Epoxica para Pisos", "9500", "10000", "2025-09-21", "Soledad Garate"],
    ["OC-8038", "Soporte Tecnico Computo", "Renovacion de Laptops", "27000", "28000", "2025-09-24", "Joel Lopez"],
    ["OC-8039", "Valvulas de Control Hidraulico", "Actuadores Neumaticos", "15900", "15000", "2025-09-27", "Soledad Garate"],
    ["OC-8040", "Transportes Logisticos Express", "Envios Urgentes Provincia", "6800", "7000", "2025-09-30", "Joel Lopez"],
    ["OC-8041", "Termometros y Sensores S.A.", "Termocuplas para Extrusoras", "8200", "8000", "2025-08-04", "Soledad Garate"],
    ["OC-8042", "Calderas y Vapor EIRL", "Mantenimiento de Caldero", "21500", "22000", "2025-08-07", "Joel Lopez"],
    ["OC-8043", "Baterias y UPS del Peru", "Banco de Baterias UPS", "14900", "15000", "2025-08-10", "Soledad Garate"],
    ["OC-8044", "Estructuras Metalicas Pro", "Mezzanine de Almacen", "48000", "45000", "2025-08-13", "Joel Lopez"],
    ["OC-8045", "Servicios de Ingenieria Avanzada", "Consultoria de Procesos", "20000", "20000", "2025-08-16", "Soledad Garate"],
    ["OC-8046", "Mangueras y Conexiones High", "Mangueras de Alta Presion", "6100", "6000", "2025-08-19", "Joel Lopez"],
    ["OC-8047", "Control de Plagas Industrial", "Fumigacion de Planta", "3800", "4000", "2025-08-22", "Soledad Garate"],
    ["OC-8048", "Dispositivos de Red Enterprise", "Switches Cisco Catalyst", "26000", "25000", "2025-08-25", "Joel Lopez"],
    ["OC-8049", "Empaques Flexibles del Sur", "Bolsas de Polietileno", "11200", "11000", "2025-08-28", "Joel Lopez"],
    ["OC-8050", "Servicios Generales Planta", "Reparacion de Techos", "17000", "17500", "2025-08-31", "Soledad Garate"]
]

archivo = os.path.join("data", "raw", "ordenes_compra_2025.csv")

with open(archivo, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id_orden", "proveedor", "categoria_insumo", "monto_ejecutado", "monto_presupuestado", "fecha_emision", "gestor"])
    writer.writerows(datos_ordenes)

print("=" * 60)
print("EXTRACT (CAPA RAW) - CIPSA CIPTECH")
print("=" * 60)
print(f"Fecha de ejecucion: {datetime.now()}")
print(f"Total de ordenes de compra extraidas: {len(datos_ordenes)}")
print(f"Archivo generado: {archivo}")