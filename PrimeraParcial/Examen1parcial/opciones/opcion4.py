import os
import time
from funciones.modificar import verificar_id, verificar_opc
from funciones.consultar import consultar
from opciones.opcion6 import opcion6 



def opcion4(opc2:int, ids:list, existencias:list) -> int:
    while opc2!=2:
        os.system("cls")
        print("######### Prototipo de Sistema de Inventarios para Tienda Departamental. #########\n")
        print("4) Consultar las existencias por ID.")
        try:
            id = int(input("Introduce el ID: "))
            if verificar_id(id,ids)==True:
                consultar(id,ids,existencias)
        except:
            print("El ID es incorrecto, vuelve a ingresarlo, digite 1 para volver a comenzar")
        try:
            opc2 = int(input("\nDigite 1 para consultar otro articulo\nDigite 2 para finalizar el programa.\nDigite 3 para regresar al menu.\nOpcion: "))
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
