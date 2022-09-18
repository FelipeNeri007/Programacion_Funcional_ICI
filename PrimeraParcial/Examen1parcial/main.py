# Cristian Armando Larios Bravo
# Haciendo y probando codigos chidos
import os
import time
from opciones.opcion1 import opcion1
from opciones.opcion2 import opcion2
from opciones.opcion3 import opcion3
from opciones.opcion4 import opcion4
from opciones.opcion5 import opcion5
from opciones.opcion6 import opcion6

if __name__ == "__main__":
    
    opc = 0 # Para correr las opciones del menu principal
    opc2 = 0 # Para correr las opciones de retorno

    ids = []
    nombres_articulos = []
    precios_unitarios = [] 
    existencias = []

    while True:
        while True:
            os.system("cls")
            print("######### Prototipo de Sistema de Inventarios para Tienda Departamental. #########\n")
            print("1) Dar de alta un articulo con su ID, nombre articulo, precio unitario y existencia.")
            print("2) Modificar un articulo con cualquiera de sus datos (menos el ID).")
            print("3) Eliminar un articulo de manera logica o fisica de acuerdo con su ID.")
            print("4) Consultar las existencias por ID.")
            print("5) Inventario Final.")
            print("6) Salir.")

            try:
                opc = int(input("Introduce la opcion: "))
            except:
                print("\nOpcion no valida, introduce de nuevo la opcion...5...4...3...2...1")
                time.sleep(5)

            if opc == 1 or opc == 2 or opc == 3 or opc == 4 or opc == 5 or opc == 6:
                os.system("cls")
                break
        match opc:
            case 1: #Done
                opcion1(opc2, ids, nombres_articulos, precios_unitarios, existencias)
            case 2: #Done
                opcion2(opc2, ids, nombres_articulos, precios_unitarios, existencias)
            case 3: #Done
                opcion3(opc2, ids, nombres_articulos, precios_unitarios, existencias)               
            case 4: #Done
                opcion4(opc2, ids, existencias)
            case 5: #Done
                opcion5(opc2, ids, nombres_articulos, precios_unitarios, existencias)
            case 6: #Done
                opcion6()

# Cristian Larios © 
