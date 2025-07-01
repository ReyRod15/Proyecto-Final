import msvcrt
import time
from tabulate import tabulate
from utilidades import generar_id, pedir_precio_valido
from archivo import guardar_inventario
from reporte import registrar_cambio

def agregar_producto(inventario): # Esta funcion agrega un producto nuevo
    nombre = input("Nombre de producto nuevo: ")
    nombre = nombre.capitalize()
    cantidad = int(input("Cantidad del producto: (Luego indicara la medida del producto si es en metros, miligramos, etc): "))
    time.sleep(0.05)
    print("\nOpciones de medidas para productos:")
    print("1. Metros")
    time.sleep(0.05)
    print("2. Miligramos")
    time.sleep(0.05)
    print("3. Unitario")
    time.sleep(0.05)
    print("4. Otro")
    opcion = 0
    while opcion not in [1, 2, 3, 4]:
        opcion = int(input("\nEscriba el número de la medida que desea emplear: "))
        if opcion == 1:
            unidad_medida = "m"
        elif opcion == 2:
            unidad_medida = "mg"
        elif opcion == 3:
            unidad_medida = "Unid"
        elif opcion == 4:
            unidad_medida = str(input("\nEscriba la medida del producto: "))
        else:
            print("\nSeleccione una opción valída")
        
    precio_unit = pedir_precio_valido()
    precio_total = precio_unit * cantidad
    minimo = int(input("\n¿Cuál es el mínimo en existencias permitido de este producto?: "))
    nuevo_id = generar_id(inventario, nombre)
    
    inventario[nuevo_id] = {
        "nombre": nombre,
        "cantidad": cantidad,
        "unidad_medida": unidad_medida,
        "precio_unit": precio_unit,
        "precio_total": precio_total,
        "minimo": minimo
    }
    guardar_inventario(inventario)
    registrar_cambio(f"Producto #{nuevo_id} - {nombre} agregado con {cantidad} {unidad_medida}")
    print(f"Producto {nombre}, agregado con éxito")

def mostrar_productos(inventario):
    tabla_productos = []    #Crea matriz para ingresar las listas creadas posteriormente
    precios_totales = 0     #Total en dolares de todos los productos
    for id_, datos in inventario.items():  #Bucle para guardar crear una lista por cada id, para que lo procese bien tabulate
        cantidad = datos["cantidad"]
        medida = datos["unidad_medida"]
        fila_id = [  #Crea una lista para cada item en orden para poder procesarlo en la tabla de tabulate
            id_,
            datos["nombre"],
            f"{cantidad} {medida}",    #Se separa la unidad de medida de la cantidad para que sea un int
            f"{datos['precio_unit']:.2f}$",
            f"{datos['precio_total']:.2f}$"
        ]
        precios_totales += datos['precio_total']   #Acumulador de los totales de cada producto
        tabla_productos.append(fila_id)

    total_tabla = ["", "", "", "Total ---->", f"{precios_totales}$"]
    tabla_productos.append(total_tabla)
    print(tabulate(tabla_productos, headers=['ID', 'Producto', 'Cantidad', 'Precio Unitario', 'Precio Total'], tablefmt='grid'))


def borrar_producto(inventario):
    print("\nEscriba el ID del producto que desea borrar, las opciones son las siguientes: ")
    mostrar_productos(inventario)
    encontrado = False
    while encontrado == False:
        producto_borrar = str(input("\nEscriba el ID: ")).capitalize()
        for i in inventario.keys():
            if producto_borrar == i:
                encontrado = True
                for id_, datos in inventario.items():
                    if id_ == producto_borrar:
                        nombre = datos["nombre"]
                        cantidad = datos["cantidad"]
                        precio = datos["precio_unit"]
                        print(f"\n¿Seguro que quiere borrar {datos["nombre"]}, permanentemente del inventario?")
                        doble_veri = str(input("\nEscriba 'CONFIRMAR' para proceder: "))
                        if doble_veri == "CONFIRMAR":
                            del inventario[producto_borrar]
                            print("\n======= Producto borrado con exito =======")
                            break
                        else:
                            print("\nProceso cancelado")
                break
        if not encontrado:
            print("\nId de producto no existente, por favor ingreselo de nuevo")
    guardar_inventario(inventario)
    registrar_cambio(f"Producto #{producto_borrar.capitalize()} borrado -- nombre: {nombre} - cantidad: {cantidad} - precio: {precio}")

def actu_precios(inventario):
    while True:
        print("Desea:")
        time.sleep(0.3)
        print("1. Actualizar todos precios")
        print("2. Cambiar el precio de un producto específico")
        opcion = input("\nEscriba el número de la opción que desea ejecutar: ")
                    
        if opcion == "1":
            for id_, datos in inventario.items():
                print(f"\nA que precio desea cambiar el siguiente producto '{datos["nombre"]}'")
                print(f"Precio actual >>> {datos["precio_unit"]}")
                try:
                    datos["precio_unit"] = pedir_precio_valido("Nuevo precio: ")
                    print(f"====== Precio de '{datos["nombre"]}', cambiado con éxito a {datos["precio_unit"]}$ ======")
                    print()
                    registrar_cambio(f"Cambio de precio de producto #{id_} - nombre: {datos["nombre"]} a {datos["precio_unit"]}$")
                except ValueError:
                    print("Escribe un caracter valído")
            guardar_inventario(inventario)
            break
        elif opcion == "2":
            print("\nProductos disponibles")
            time.sleep(0.5)
            mostrar_productos(inventario)
            while True:
                eleccion = str(input("\nEscriba el ID: ")).capitalize()
                if eleccion in inventario:
                    datos = inventario[eleccion]
                    precio_anterior = datos["precio_unit"]
                    nuevo_precio = pedir_precio_valido(f"Nuevo precio para {datos['nombre']}: ")
                    datos["precio_unit"] = int(nuevo_precio)
                    datos["precio_total"] = datos["precio_unit"] * datos["cantidad"]
                    print(f"\n===== Precio de '{datos["nombre"]}' cambiado con éxito de {precio_anterior}$ a {datos["precio_unit"]}$ =====")
                    guardar_inventario(inventario)
                    registrar_cambio(f"Cambio de precio de producto #{eleccion} - nombre: {datos["nombre"]} a {datos["precio_unit"]}$")
                    break
                else:
                    print("\nId no encontrado, intentelo de nuevo")
            break
        else:
            print()
            print('\nOpción invalida, escoga 1 o 2')


def cambiar_datos(inventario):
    mostrar_productos(inventario)
    while True:
        try:
            eleccion = str(input("\nEscriba el ID: ")).capitalize()
            if eleccion in inventario:
                print(f"¿Qué desea cambiar del producto ID# '{eleccion}'?")
                print("\nOpciones")
                print("\n1. Nombre")
                print("2. Cantidad")
                print('3. Precio')
                print("4. Minimo")
                print("5. Unidad de medida")
                opcion = str(input("\nEscriba el número de la opción que desea: "))
                if opcion == "1":
                    inventario[eleccion]["nombre"] = str(input(f"Escriba el nuevo nombre para el producto ID# {eleccion}: "))
                    print(f"\n======= Nombre cambiado con éxito a {inventario[eleccion]["nombre"]} =======")
                    guardar_inventario(inventario)
                    registrar_cambio(f"Cambio de nombre de producto #{eleccion} a {inventario[eleccion]["nombre"]}")
                    break
                elif opcion == "2":
                    inventario[eleccion]["cantidad"] = int(input(f"Ingrese la nueva cantidad para el producto ID# {eleccion}: "))
                    inventario[eleccion]["precio_total"] = inventario[eleccion]["precio_unit"] * inventario[eleccion]["cantidad"]
                    print(f"\n======= Cantidad actualizada a {inventario[eleccion]["cantidad"]} {inventario[eleccion]["unidad_medida"]} =======")
                    guardar_inventario(inventario)
                    registrar_cambio(f"Cambio de cantidad de producto #{eleccion} - nombre: {inventario[eleccion]["nombre"]} - nueva cantidad: {inventario[eleccion]["cantidad"]}")
                    break
                elif opcion == "3":
                    inventario[eleccion]["precio_unit"] = int(input(f"Ingrese el nuevo precio para el producto ID# {eleccion}: "))
                    inventario[eleccion]["precio_total"] = inventario[eleccion]["precio_unit"] * inventario[eleccion]["cantidad"]
                    print(f"\n======= Precio actualizado a {inventario[eleccion]["precio_unit"]} por {inventario[eleccion]["unidad_medida"]} =======")
                    guardar_inventario(inventario)
                    registrar_cambio(f"Cambio de precio de producto #{eleccion} - nombre: {inventario[eleccion]["nombre"]} - nuevo precio: {inventario[eleccion]["precio_unit"]}$")
                    break
                elif opcion == "4":
                    inventario[eleccion]["minimo"] = int(input(f"Ingrese el nuevo minímo para el producto ID# {eleccion}: "))
                    print(f"\n=======  Minimo actualizado a {inventario[eleccion]["minimo"]}{inventario[eleccion]["unidad_medida"]} =======")
                    guardar_inventario(inventario)
                    registrar_cambio(f"Cambio de minimo de producto #{eleccion} - nombre: {inventario[eleccion]["nombre"]} - nuevo minimo: {inventario[eleccion]["minimo"]}")
                    break
                elif opcion == "5":
                    inventario[eleccion]["unidad_medida"] = str(input(f"Ingrese la nueva unidad de medida (m, Unid, mg, etc) en el producto ID# {eleccion}: "))
                    print(f"\n======= Unidad de medida actualizada a {inventario[eleccion]["unidad_medida"]} =======")
                    guardar_inventario(inventario)
                    registrar_cambio(f"Cambio de minímo de producto #{eleccion} - nombre: {inventario[eleccion]["nombre"]} - nueva unidad de medida: {inventario[eleccion]["unidad_medida"]}")
                    break
                else:
                    print("\nEscoja una opción valída")
            else:
                print("\nId no encontrado, intente de nuevo")
        except ValueError:
                    print("\nEscribe un caracter valído")


def compra_venta(inventario):
    print("\nOpciones")
    print("1. Comprar")
    print("2. Vender")
    print("3. Volver al menú")
    while True:
        try:
            eleccion = int(input("\n¿Quieres comprar o vender?: "))
            if eleccion == 1:
                while True:
                    mostrar_productos(inventario)
                    producto = str(input("\nIngrese el ID del producto a comprar: ")).capitalize()
                    if producto in inventario:
                        cantidad_comprar = int(input(f"\nCuanto del producto '{inventario[producto]["nombre"]}' quiere comprar: "))
                        inventario[producto]["cantidad"] += cantidad_comprar
                        inventario[producto]["precio_total"] = inventario[producto]["precio_unit"] * inventario[producto]["cantidad"]
                        guardar_inventario(inventario)
                        registrar_cambio(f"Se compro {cantidad_comprar} {inventario[producto]["unidad_medida"]} del producto #{producto}")
                        print("\n=========== Producto comprado con exito ===========")
                        print()
                        return
                    else:
                        print("\nId no valido, intente de nuevo")
                        print("\nPresiona cualquier tecla para continuar...")
                        msvcrt.getch()
            elif eleccion == 2:
                while True:
                    mostrar_productos(inventario)
                    producto = str(input("\nIngrese el ID del producto a vender: ")).capitalize()
                    if producto in inventario:
                        cantidad_vender = int(input(f"\nCuanto del producto '{inventario[producto]["nombre"]}' quiere vender: "))
                        if cantidad_vender <= inventario[producto]["cantidad"]:
                            inventario[producto]["cantidad"] -= cantidad_vender
                            inventario[producto]["precio_total"] = inventario[producto]["precio_unit"] * inventario[producto]["cantidad"]
                            guardar_inventario(inventario)
                            registrar_cambio(f"Se vendio {cantidad_vender} {inventario[producto]["unidad_medida"]} del producto #{producto}")
                            print("\n=========== Producto vendido con exito ===========")
                            print()
                            return
                        else:
                            print(f"\nCantidad superior a existencias actuales, stock actual: {inventario[producto]["cantidad"]} {inventario[producto]["unidad_medida"]}")
                    else:
                        print("\nId no valído, intente de nuevo")
                        print("\nPresiona cualquier tecla para continuar...")
                        msvcrt.getch()
            elif eleccion == 3:
                print("Volviendo al menú...")
                print()
                break
            else:
                print("\nOpción no valída escoja una de las opciones anteriores")
        except ValueError:
                    print("\nEscribe un caracter valído")