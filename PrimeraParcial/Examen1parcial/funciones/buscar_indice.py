def buscar_indice(id:int,ids:list)->int: 
    if id in ids:
        return ids.index(id)