import pyfiglet
import msvcrt
import time
from archivo import cargar_inventario
from inventario import mostrar_productos, agregar_producto, borrar_producto, actu_precios, cambiar_datos
from reporte import alerta_min
def main():
    def menu():
        inventario = cargar_inventario()
        print(pyfiglet.figlet_format("Inventario", font="slant"))
        presentacion = [
            "Menu de Opciones",
            "1. Mostrar los productos",
            "2. Agregar Producto",
            "3. Borrar Producto",
            "4. Actualizar precios",
            "5. Reporte de Movimientos",
            "6. Cambiar Datos de un Producto",
            "7. Ultimo Cambio hecho",
            "8. Salir"
        ]
        opcion = 0
        while opcion != 8:
            print()
            for linea in presentacion:
                for letra in linea:
                    print(letra, end='', flush=True)
                    time.sleep(0.007)
                print()
            try:
                opcion = int(input("\nSeleccione un numero, Que desea hacer?: "))
                if opcion == 1:
                    mostrar_productos(inventario)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 2:
                    agregar_producto(inventario)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 3:
                    borrar_producto(inventario)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 4:
                    actu_precios(inventario)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 5:
                    #Funcion por crearse (Reporte)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 6:
                    cambiar_datos(inventario)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 7:
                    #Funcion por crearse
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 8:
                    [print(c, end='', flush=True) or time.sleep(0.05) for c in "Saliendo del Programa, Gracias por todo :)"]
                else:
                    print("\nEscoge una opcion valida")
                    time.sleep(1)
                    print("")
            except ValueError:
                print()
                print("\nSelecciona una opcion valida")
    menu()

if __name__ == "__main__":
    main()