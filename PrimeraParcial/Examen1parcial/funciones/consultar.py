from funciones.buscar_indice import buscar_indice

def consultar(id:int,ids:list,existencias:list) -> list:
    xr = buscar_indice(id,ids)
    print(f"{'ID':^{12}} {'Nombre':^{12}} {'Precio c/u':^{12}} {'Existencias':^{12}}")
    print(f"{ids[xr]:^{12}} {'':^{12}} {'':^{12}} {existencias[xr-1]:^{12}}")
    return existencias