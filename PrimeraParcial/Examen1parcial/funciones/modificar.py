from funciones.buscar_indice import buscar_indice

def modificar_nombre(id:int,ids:list, cambio_nombre:str, nombres_articulos:list)->list:
    xr = buscar_indice(id, ids) 
    nombres_articulos[xr] = cambio_nombre

def modificar_precio(id:int,ids:list,cambio_precio:float, existencias:list) -> list:
    xr = buscar_indice(id, ids)
    existencias[xr] = cambio_precio

def modificar_existencias(id:int,ids:list,cambio_existencia:int, precios_unitarios:list) ->list:
    xr = buscar_indice(id, ids)
    precios_unitarios[xr] = cambio_existencia

def verificar_id(id:int,ids:list) -> bool:
    if id in ids:
        return True
    else:
       while(id not in ids):
        print("El ID no existe en la base de datos")
        return False

def verificar_opc(opc:int) -> int: ###
    if opc==1 or opc==2 or opc==3:
        return opc
    while opc!=1 or opc!=2 or opc!=3:
            opc = int(input("Opcion no valida, digite una nueva opcion: "))
            if opc==1 or opc==2 or opc==3:
                return opc

def verificar_opc_inv(opc:int) -> int:
    if opc==1 or opc==2:
        return opc
    while opc!=1 or opc!=2:
            opc = int(input("Opcion no valida, digite una nueva opcion: "))
            if opc==1 or opc==2:
                return opc

def verificar_existencias(num:int) ->int:
    while num<0:
        num = int(input("Las existencias no pueden ser negativo, ingresalo de nuevo: $"))
    return num

def verificar_precio(num:float) -> float:
    while num<0:
        num = int(input("El precio no puede ser negativo, ingresalo de nuevo: $"))
    return num
