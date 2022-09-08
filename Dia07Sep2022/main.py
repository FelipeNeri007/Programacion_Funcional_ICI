# Dia 02 de Septiembre de 2022


""" materias = ["Nombre", "Est Dat", "Prog Func", "Ingles"]
alumnos = ["Hugo Alberto", "Paco", "Luis", "Lupita"]
materia1 = [9,7,9,8]
materia2 = [8,9,7,8]
materia3 = [6,7,9,8]


def calificaciones(ancho:int) -> str:
    print(f"{materias[0]:^{ancho}} {materias[1]:^{ancho}} {materias[2]:^{ancho}} {materias[3]:^{ancho}}")
    for i in range(len(alumnos)):
        print(f"{alumnos[i]:*<{ancho}} {materia1[i]:+^{ancho}} {materia2[i]:#>{ancho}} {materia3[i]:-^{ancho}}")
    return 0

if __name__ == "__main__":
    ancho = 15
    calificaciones(ancho) """

""" # Separacion con comas
numeroBig = 123456789123456787
print(f"{numeroBig:,d}")
# Notacion cientifica
numeroPI = 3.141592653589793
print(f"{numeroPI:.3f}")
numeroPI = 314.1592653589793
print(f"{numeroPI:e}")
print(f"{numeroPI:.2e}")
# Porcentaje
numeroPorciento = 0.258478585
print(f"{numeroPorciento:%}")
print(f"{numeroPorciento:.2%}")

#Numeros Binarios
print(f"{25:b}")
#Unicodes
print(f"{13:c}")
#Hexadecimal
print(f"{255:x}")
#Octal
print(f"{255:o}")
 """

'''
Escriba una funcion que genere una tabla de multiplicar recibiendo como argumento la cantidad de numeros y la tabla a generar
'''

""" def multiplicar2numeros(x:int,y:int)->int: return x*y

def tablamultiplicar(num:int,total:int)->int:
    print(f"Tabla de multiplicar del {num}")
    for i in range(1, total+1):
        print(f"{num:<3}x{i:^4}={multiplicar2numeros(i,num):>4}")
    return 0

def multitablas(numtablas:int,num:int,total:int)->int:
    print(f"Tablas de multiplicar de {num} hasta {numtablas}")
    for i in range(1, numtablas+1):
        tablamultiplicar(num,total)
        print()
        num+=1
    return 0

if __name__ == "__main__":
    tablamultiplicar(1, 10)
    multitablas(10, 2, 10) """


############################################################################################################################################
# Dia 07 de Septiembre de 2022

lista1 = [1, 2, 3, 4]
print(lista1)

lista2 = [1, 3.14, "a", True, [1,2,3], (1, 2, 3), {8, "a", 5.4}]
print(lista2)

print(len(lista1))

print(len(lista2))
print(lista2[6])

lista_cal = []
print(lista_cal)
lista_cal.append(5)
print(lista_cal)
lista_cal.append(8)
print(lista_cal)
lista_cal.insert(0,6)
lista_cal.append(5)
print(lista_cal)

# Rellenar una lista con los numeros naturales del 1 al 10

lista6 = []

for i in range(1,11):
    lista6.append(i)

print(lista6)

# Imprimir un elemento de la lista al reves con indices negativos
print(lista1[-4])

# Slices (rebanadas)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista1)
print(lista1[:])
print(lista1[0:10])
print(lista1[int(len(lista1)/2):])
print(lista1[:int(len(lista1)/2)])
print(lista1[0:-1])
print(lista1[3:7])
print(lista1[-7:-3])

print("---------------------------------")
lista1 = [1, "dos", 3, "cuatro"]
lista2 = lista1

print(f"Lista 1: {lista1}")
print(f"Lista 1: {lista2}")
print()
print(f"Direccion lista1: {id(lista1)}")
print(f"Direccion lista2: {id(lista2)}")
print()
# lista1[1] = 2
# lista1[3] = 4
print("---------------------------------")
print(f"Lista 1: {lista1}")
lista2 = lista1[:]
lista2[1] = 2
lista2[3] = 4 
print(f"Lista 2: {lista2}")
print("")
print(f"Direccion lista1: {id(lista1)}")
print(f"Direccion lista1: {id(lista2)}")
print("---------------------------------")

lista1 = [0,1,2,3,4]
lista2 = [5,6,7]
# lista1[5:] = lista2
# lista1.extend([5,6,7])
#lista1[len(lista1):] = lista2
""" 
for i in range(5,8):
    lista1.append(i)
 """
 # Insertar al inicio de la lista varios elementos (en una lista)
# lista1[:0] = lista2
# print(lista1)

# lista1.append(lista2)
lista1.extend(lista2)
print(lista1)

# del(lista1[0])  # Eliminar la lista1 indice 0
del lista1[0]  # Eliminar la lista1 indice 0
print(lista1)
del(lista1[2:5])
print(lista1)