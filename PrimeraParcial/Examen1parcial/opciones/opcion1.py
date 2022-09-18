import os
import time
from funciones.alta import alta
from funciones.modificar import verificar_opc
from opciones.opcion6 import opcion6

def opcion1(opc2:int, ids:list, nombres_articulos:list, precios_unitarios:list, existencias:list) -> int:
    while opc2!=2:
        os.system("cls")
        print("######### Prototipo de Sistema de Inventarios para Tienda Departamental. #########\n")
        print("1) Dar de alta un articulo con su ID, nombre articulo, precio unitario y existencia.")
        try:
            id = int(input("Ingresa el ID: "))
            nombre_articulo = str(input("Ingresa el nombre del articulo: "))
            precio_unitario = float(input("Ingresa el precio unitario del articulo: $"))
            existencia = int(input("Ingrese las existencias del articulo: "))
            alta(id, nombre_articulo, precio_unitario, existencia, ids, nombres_articulos, precios_unitarios, existencias)
        except:
            print("Los datos ingresados son incorrectos, digite 1 para volver a iniciar.")
        try:
            opc2 = int(input("\nDigite 1 para agregar otro articulo\nDigite 2 para finalizar el programa.\nDigite 3 para regresar al menu.\nOpcion: "))
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