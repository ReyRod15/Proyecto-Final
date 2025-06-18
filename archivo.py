import os
import json

ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventario.json")

def cargar_inventario():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {}

def guardar_inventario(inventario):
    with open(ARCHIVO, "w") as f:
        json.dump(inventario, f, indent=4)
