import os
import time
from funciones.modificar import verificar_opc_inv
from funciones.inventario import inventario
from opciones.opcion6 import opcion6

def opcion5(opc2:int,ids:list,nombres_articulos:list,precios_unitarios:list,existencias:list) ->int:
    while opc2!=2:
        os.system("cls")
        print("######### Prototipo de Sistema de Inventarios para Tienda Departamental. #########\n")
        print(f"5) {'INVENTARIO FINAL':^{48}}")
        try:
            inventario(ids, nombres_articulos, precios_unitarios, existencias)
        except (ValueError, TypeError, IndexError):
            print("Datos incorrectos en el inventario")
        try:
            opc2 = int(input("\nDigite 1 para finalizar el programa.\nDigite 2 para volver al menu\nOpcion: "))
            opc2 = verificar_opc_inv(opc2)
            if opc2 == 1:
                opcion6()
            else:
                break
        except (ValueError, TypeError, IndexError):
            print("Opcion invalida, regresando al menu...5...4...3...2...1")
            time.sleep(5)
            os.system("cls")
            break