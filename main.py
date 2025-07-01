import pyfiglet
import msvcrt
import time
from archivo import cargar_inventario
from inventario import mostrar_productos, agregar_producto, borrar_producto, actu_precios, cambiar_datos, compra_venta
from reporte import alerta_min, mostrar_registro
def main():
    def menu():
        inventario = cargar_inventario()
        print(pyfiglet.figlet_format("Inventario", font="slant"))
        presentacion = [
            "Menu de Opciones",
            "1. Mostrar productos",
            "2. Agregar producto",
            "3. Borrar producto",
            "4. Actualizar precios",
            "5. Reporte de movimientos",
            "6. Cambiar datos de un producto",
            "7. Comprar/Vender productos",
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
                opcion = int(input("\nSeleccione un número, Que desea hacer?: "))
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
                    mostrar_registro()
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 6:
                    cambiar_datos(inventario)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 7:
                    compra_venta(inventario)
                    alerta_min(inventario)
                    print("\nPresiona cualquier tecla para continuar...")
                    msvcrt.getch()
                elif opcion == 8:
                    [print(c, end='', flush=True) or time.sleep(0.05) for c in "Saliendo del Programa, Gracias por todo :)"]
                else:
                    print("\nEscoge una opción valída, 1 al 8")
                    time.sleep(1)
                    print("")
            except ValueError:
                print()
                print("\nSelecciona un número valído")
    menu()

if __name__ == "__main__":
    main()