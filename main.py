import pyfiglet
import msvcrt
import time
from archivo import cargar_inventario
from operaciones import mostrar_productos, agregar_producto, borrar_producto, actu_precios
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