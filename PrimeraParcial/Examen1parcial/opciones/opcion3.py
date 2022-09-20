import os
import time
from funciones.modificar import verificar_id, verificar_opc
from funciones.eliminar import eliminar
from opciones.opcion6 import opcion6

def opcion3(opc2:int, ids:list, nombres_articulos:list, precios_unitarios:list, existencias:list) -> int:
    while opc2!=2:
        os.system("cls")
        print("######### Prototipo de Sistema de Inventarios para Tienda Departamental. #########\n")
        print("3) Eliminar un articulo de manera logica o fisica de acuerdo con su ID.")
        try:
            id = int(input("Introduce el ID: "))
            if verificar_id(id,ids)==True:
                eliminar(id,ids,nombres_articulos,precios_unitarios,existencias)
        except:
            print("El ID es incorrecto, digite 1 para volver a comenzar.")
        try:
            opc2 = int(input("\nDigite 1 para eliminar otro articulo\nDigite 2 para finalizar el programa.\nDigite 3 para regresar al menu.\nOpcion: "))
            opc2 = verificar_opc(opc2)
            if opc2 == 1:
                opc2 = 90
                pass
            elif opc2 == 2:
                opcion6()
            else:
                break
        except:
            print("Opcion invalida, regresando al menu principal...5...4...3...2...1")
            time.sleep(5)
            os.system("cls")
            break