def inventario(ids:list, nombres_articulos:list, precios_unitarios:list, existencias:list) ->str:
    print(f"{'ID':^{12}} {'Nombre':^{12}} {'Precio c/u':^{12}} {'Existencias':^{12}}")
    for i in range(len(ids)):
        print(f'{ids[i]:^{12}} {nombres_articulos[i]:^{12}} {precios_unitarios[i]:^{12}} {existencias[i]:^{12}}')
    
    if ids == [] and nombres_articulos == [] and precios_unitarios == [] and existencias == []:
        print(f"{' INVENTARIO VACIO ':#^{50}}")
