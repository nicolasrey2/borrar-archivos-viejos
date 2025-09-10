#!/usr/bin/env python3
import os
import time
import argparse

# ----------------------
# Configuración por argumentos
# ----------------------
parser = argparse.ArgumentParser(description="Borrar archivos viejos en un directorio")
parser.add_argument("-d", "--dir", required=True, help="Directorio a limpiar")
parser.add_argument("-t", "--dias", type=int, required=True, help="Número de días para conservar archivos")
args = parser.parse_args()

DIR = args.dir
DIAS = args.dias

# ----------------------
# Cálculo de tiempo límite
# ----------------------
ahora = time.time()
limite = ahora - (DIAS * 86400)  # 86400 segundos = 1 día

# ----------------------
# Iterar solo archivos
# ----------------------
with os.scandir(DIR) as it:
    for entry in it:
        if entry.is_file() and entry.stat().st_atime < limite:
            try:
                os.remove(entry.path)
                print(f"Eliminado: {entry.path}")
            except Exception as e:
                print(f"No se pudo eliminar {entry.path}: {e}")
