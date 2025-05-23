import json
import os
from tabulate import tabulate
import random
import time

ARCHIVO = "inventario.json"

# FUNCIONES DE ARCHIVO


def cargar_inventario():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {}

def guardar_inventario(inventario):
    with open(ARCHIVO, "w") as f:
        json.dump(inventario, f, indent=4)






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



def agregar_producto(inventario): # Esta funcion agrega un producto nuevo
    nombre = input("Nombre de producto nuevo: ")
    nombre = nombre.capitalize()
    cantidad = int(input("Cantidad del producto: (Luego indicara la medida del producto si es en metros, miligramos, etc)"))
    time.sleep(1)
    print("\nOpciones de medidas para productos:")
    print("1. Metros")
    print("2. Miligramos")
    print("3. Unitario")
    print("4. Otro")
    opcion = input("Escriba el numero de la medida que desea emplear: ")
    if opcion == 1:
        cantidad = str(cantidad) + "m"
    elif opcion == 2:
        cantidad = str(cantidad) + "mg"
    elif opcion == 3:
        cantidad = str(cantidad) + "Unid"
    elif opcion == 4:
        cantidad = str(cantidad) + input("Escriba la medida del producto: ")
        

    precio_unit = float(input("Ingrese el precio del nuevo producto: "))
    precio_total = precio_unit * cantidad
    nuevo_id = generar_id(inventario, nombre)
    
    inventario[nuevo_id] = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio_unit": precio_unit,
        "precio_total": precio_total
    }
    guardar_inventario(inventario)
    print(f"Producto {nombre}, agregado con exito")




def mostrar_productos(inventario):
    tabla_productos = []
    precios_totales = 0     #Total en dolares de todos los productos
    for id_, datos in inventario.items():
        fila_id = [  #Crea una lista para cada item en orden para poder procesarlo en la tabla de tabulate
            id_,
            datos["nombre"],
            datos["cantidad"],
            f"{datos['precio_unit']:.2f}",
            f"{datos['precio_total']:.2f}"
        ]
        precios_totales += datos['precio_total']   #Acumulador de los totales de cada producto
        tabla_productos.append(fila_id)

    total_tabla = ["", "", "", "Total ---->", precios_totales]
    tabla_productos.append(total_tabla)
    tabla_excel = tabulate(tabla_productos, headers=['ID', 'Producto', 'Cantidad', 'Precio Unitario', 'Precio Total'], tablefmt='excel')
    print(tabulate(tabla_productos, headers=['ID', 'Producto', 'Cantidad', 'Precio Unitario', 'Precio Total'], tablefmt='grid'))

def borrar_producto(inventario):
    print("\nEscriba el id del producto que desea borrar, las opciones son las siguientes: ")
    mostrar_productos(inventario)
    producto_borrar = str(input("--->"))
    for i in inventario.keys():
        print(i)
        if producto_borrar == i:
            del inventario[producto_borrar]
            print("Producto borrado con exito")
            break
    guardar_inventario(inventario)

print("Prueba de commits")

inventario = cargar_inventario()
agregar_producto(inventario)
agregar_producto(inventario)
agregar_producto(inventario)
agregar_producto(inventario)
agregar_producto(inventario)
agregar_producto(inventario)
mostrar_productos(inventario)