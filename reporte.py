import datetime

def alerta_min(inventario):
    for nombre, datos in inventario.items():
        if datos["cantidad"] < datos["minimo"]:
            print(f"\nAlerta: {nombre} está por debajo del mínimo ({datos['cantidad']}/{datos['minimo']})")


def registrar_cambio(mensaje):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("reporte.txt", "a") as archivo:
        archivo.write(f"[{fecha}] {mensaje}\n")

def mostrar_registro():
    try:
        with open("reporte.txt", "r") as archivo:
            print("\n===== HISTORIAL DE CAMBIOS =====\n")
            print(archivo.read())
    except FileNotFoundError:
        print("No hay historial todavía.")
