import os
import time
from funciones.modificar import *
from opciones.opcion6 import opcion6

def opcion2(opc2:int, ids:list, nombres_articulos:list, precios_unitarios:list, existencias:list) -> int:
    while opc2!=2:
        os.system("cls")
        print("######### Prototipo de Sistema de Inventarios para Tienda Departamental. #########\n")
        print("2) Modificar un articulo con cualquiera de sus datos (menos el ID).")
        try:
            id = int(input("Introduce el ID: "))
            if verificar_id(id,ids)==True:
                qcambiar = int(input("Que deseas cambiar?\nDigite 1 para modificar el nombre.\nDigite 2 para cambiar el precio.\nDigite 3 para cambiar las existencias del producto.\nOpcion: "))
                qcambiar = verificar_opc(qcambiar)
                try:
                    match qcambiar:
                        case 1:
                            nombre_nuevo = str(input("Introduce el nuevo nombre: "))
                            modificar_nombre(id,ids,nombre_nuevo,nombres_articulos)
                        case 2:
                            precio_nuevo = float(input("Ingrese el nuevo precio: $"))
                            precio_nuevo = verificar_precio(precio_nuevo)
                            modificar_precio(id, ids, precio_nuevo, precios_unitarios)
                        case 3:
                            existencias_nuevas = int(input("Ingrese las nuevas existencias: "))
                            existencias_nuevas = verificar_existencias(existencias_nuevas)
                            modificar_existencias(id, ids, existencias_nuevas, existencias)
                except:
                    print("El valor dado no es valido, digite 1 para volver a comenzar.")
        except:
                print("ID u opcion a cambiar invalidos, digite 1 para volver a comenzar.")

        try:
            opc2 = int(input("\nDigite 1 para modificar otro articulo\nDigite 2 para finalizar el programa.\nDigite 3 para regresar al menu.\nOpcion: "))
            opc2 = verificar_opc(opc2)
            if opc2 == 1:
                opc2 = 90
                pass
            elif opc2 == 2:
                opcion6()
            else:
                break
        except:
            print("Opcion invalida, ingresa la opcion de nuevo...5...4...3...2...1")
            time.sleep(5)
            os.system("cls")
            break