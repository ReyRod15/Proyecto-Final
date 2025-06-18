import pyfiglet
import msvcrt
import time

def generar_id(inventario, nombre_producto):
    letra = nombre_producto[0].upper()  # primera letra en mayúscula
    ids_existentes = [
        int(i[1:]) for i in inventario.keys() if i.startswith(letra)
    ]   
    if not ids_existentes:
        nuevo_num = 1
    else:
        nuevo_num = max(ids_existentes) + 1

    return f"{letra}{nuevo_num:03d}"

def pedir_precio_valido(mensaje="Nuevo precio: "):
    while True:
        precio_nuevo = input(mensaje).strip()
        if precio_nuevo == "":
            print("No puedes dejarlo vacío.")
            continue
        if precio_nuevo.isdigit():
            precio = int(precio_nuevo)
            if precio > 0:
                return precio
            else:
                print("El precio debe ser mayor que cero.")
        else:
            print("Ingresa solo números enteros positivos.")