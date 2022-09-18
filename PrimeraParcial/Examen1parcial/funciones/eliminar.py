from funciones.buscar_indice import buscar_indice

def eliminar(id:int,ids:list, nombres_articulos:list, precios_unitarios:list,existencias:list) ->list:
    xr = buscar_indice(id, ids)
    del ids[xr]
    del nombres_articulos[xr]
    del precios_unitarios[xr]
    del existencias[xr]