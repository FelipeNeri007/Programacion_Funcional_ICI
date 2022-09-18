def alta(id:int, nombre_articulo:str, precio_unitario:float, existencia:int, ids:list, nombres_articulos:list, precios_unitarios:list,existencias:list) -> list:
    while id<1:
        id = int(input("El ID no puede ser negativo o cero, ingresalo de nuevo: "))
    while id in ids == True:
        id = int(input("El ID ya esta registrado, ingrese uno nuevo: "))
    while existencia<0:
        existencia = int(input("Las existencias no pueden ser negativas, ingresalas de nuevo: "))
    while precio_unitario<0:
        precio_unitario =int(input("El precio del articulo no puede ser negativo, ingrese de nuevo el precio: $"))
    while nombre_articulo == "":
        nombre_articulo = str(input("El nombre del articulo no puede estar vacio, ingrese de nuevo el nombre: "))
    ids.append(id)
    nombres_articulos.append(nombre_articulo)
    if precio_unitario == 0:
        precios_unitarios.append('GRATIS')
    else:
        precios_unitarios.append(precio_unitario)
    existencias.append(existencia)