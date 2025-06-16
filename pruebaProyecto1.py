import json
import os
from tabulate import tabulate
import random
import time
import pyfiglet
import msvcrt
ARCHIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventario.json")


    # FUNCIONES DE ARCHIVO
def cargar_inventario():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return {}

def guardar_inventario(inventario):
    with open(ARCHIVO, "w") as f:
        json.dump(inventario, f, indent=4)

def main():
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
        cantidad = int(input("Cantidad del producto: (Luego indicara la medida del producto si es en metros, miligramos, etc): "))
        time.sleep(0.5)
        print("\nOpciones de medidas para productos:")
        print("1. Metros")
        time.sleep(0.5)
        print("2. Miligramos")
        time.sleep(0.5)
        print("3. Unitario")
        time.sleep(0.5)
        print("4. Otro")
        cantidad_base = cantidad
        opcion = 0
        while opcion not in [1, 2, 3, 4]:
            opcion = int(input("Escriba el numero de la medida que desea emplear: "))
            if opcion == 1:
                cantidad = str(cantidad) + "m"
            elif opcion == 2:
                cantidad = str(cantidad) + "mg"
            elif opcion == 3:
                cantidad = str(cantidad) + " Unid"
            elif opcion == 4:
                cantidad = str(cantidad) + input("Escriba la medida del producto: ")
            else:
                print("\nSeleccione una opcion valida")
            
        precio_unit = float(input("Ingrese el precio del nuevo producto (teniendo en cuenta la medida que escogio anteriormente): "))
        precio_total = precio_unit * cantidad_base
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
                f"{datos['precio_unit']:.2f}$",
                f"{datos['precio_total']:.2f}$"
            ]
            precios_totales += datos['precio_total']   #Acumulador de los totales de cada producto
            tabla_productos.append(fila_id)

        total_tabla = ["", "", "", "Total ---->", precios_totales]
        tabla_productos.append(total_tabla)
        tabla_excel = tabulate(tabla_productos, headers=['ID', 'Producto', 'Cantidad', 'Precio Unitario', 'Precio Total'], tablefmt='excel')
        print(tabulate(tabla_productos, headers=['ID', 'Producto', 'Cantidad', 'Precio Unitario', 'Precio Total'], tablefmt='grid'))

    def borrar_producto(inventario):
        print("\nEscriba el ID del producto que desea borrar, las opciones son las siguientes: ")
        mostrar_productos(inventario)
        producto_borrar = str(input("Escriba el ID: "))
        for i in inventario.keys():
            if producto_borrar == i:
                del inventario[producto_borrar]
                print("Producto borrado con exito")
                break
        guardar_inventario(inventario)

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

    def actu_precios(inventario):
        while True:
            print("Desea:")
            time.sleep(0.3)
            print("1. Actualizar todos precios")
            print("2. Cambiar el precio de un producto especifico")
            opcion = input("Escriba el numero de la opcion que desea ejecutar: ")
                        
            if opcion == "1":
                for id_, datos in inventario.items():
                    print(f"A que precio desea cambiar el siguiente producto '{datos["nombre"]}'")
                    print(f"Precio actual >>> {datos["precio_unit"]}")
                    try:
                        datos["precio_unit"] = pedir_precio_valido("Nuevo precio: ")
                        print(f"Precio de '{datos["nombre"]}', cambiado con exito a {datos["precio_unit"]}")
                        print()
                    except ValueError:
                        print("Escribe un caracter valido")
                guardar_inventario(inventario)
                break
            elif opcion == "2":
                print("\nProductos disponibles")
                time.sleep(0.5)
                mostrar_productos(inventario)
                while True:
                    eleccion = str(input("Escriba el ID: ")).capitalize()
                    if eleccion in inventario:
                        datos = inventario[eleccion]
                        precio_anterior = datos["precio_unit"]
                        nuevo_precio = pedir_precio_valido(f"Nuevo precio para {datos['nombre']}: ")
                        datos["precio_unit"] = int(nuevo_precio)
                        print(f"Precio de '{datos["nombre"]}' cambiado con exito de {precio_anterior}$ a {datos["precio_unit"]}$")
                        guardar_inventario(inventario)
                        break
                    else:
                        print("Id no encontrado, intentelo de nuevo")
                break
            else:
                print()
                print('Opcion invalida, escoga 1 o 2')


    
    inventario = cargar_inventario()
    def menu():
        print(pyfiglet.figlet_format("Inventario", font="slant"))
        presentacion = [
            "Menu de Opciones",
            "1. Mostrar los productos",
            "2. Agregar Producto",
            "3. Borrar Producto",
            "4. Actualizar precios",
            "5. Mandar tabla en archivo Excel para imprimir",
            "6. Salir"
        ]
        opcion = 0
        while opcion != 6:
            print()
            for linea in presentacion:
                for letra in linea:
                    print(letra, end='', flush=True)
                    time.sleep(0.02)
                print()
            try:
                opcion = int(input("\nEscoge el numero de las opciones de lo que deseas hacer: "))
                if opcion == 1:
                    mostrar_productos(inventario)
                    print("Presiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 2:
                    agregar_producto(inventario)
                    print("Presiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 3:
                    borrar_producto(inventario)
                    print("Presiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 4:
                    actu_precios(inventario)
                    print("Presiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 5:
                    #Funcion por crearse
                    print("Presiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 6:
                    [print(c, end='', flush=True) or time.sleep(0.1) for c in "Saliendo del Programa, Gracias por todo :)"]
                else:
                    print("Escoge una opcion valida")
                    time.sleep(1)
                    print("")
            except ValueError:
                print()
                print("Selecciona una opcion valida")
    menu()

if __name__ == "__main__":
    main()