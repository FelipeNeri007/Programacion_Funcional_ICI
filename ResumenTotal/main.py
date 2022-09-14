# Dio 24 de Agosto de 2022
'''
def suma(a, b):
    return a+b

def sumap(a, b):
    print(a+b)


# entry point
if __name__ == "__main__":
    print(suma(2,2))
    sumap(3, 3)
'''

'''
x = 10
print(x, "addr:",id(x))
x = "Hola"
print(x, "addr:",id(x))

y = 10
print(y, "addr:",id(y))

z = "HOLa"
print(z,"adrr:",id(z))
'''

'''
x = 1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
x = x+1
print(x,":",id(x))
'''

# No se declara una variable, se le asigna un valor en Python
# print(x:=5)

'''
def suma1(a, b):
    return a+b

def suma2(a:int, b:int)->int:
    return a+b

print(suma1(2, 2))
print(suma2(3, 3))

def cuadrado(n: int|float)->int|float: return n*n
print(cuadrado(2))
print(cuadrado(2.2))
'''


'''
Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla "<mensaje> <nombre>"
'''

'''
def funcion1(a: str, b: str) -> str:
    return f"<{a}> <{b}>"
'''

'''
Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: "Hola <nombre> tienes <edad> años
'''

'''
def funcion2(a: str, b: int) -> str:
    return f"Hola {a} tienes {b} años"
'''

'''
Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años"
'''

'''
def funcion3(a: int, b: int, c: str) -> str:
    edad = a - b
    return funcion2(c, edad)
'''


'''
if __name__ == "__main__":
    print("Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla '<mensaje> <nombre>'")
    print(funcion1("Hola", "Cristian"))
    print(
        "Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: 'Hola <nombre> tienes <edad> años'")
    print(funcion2("Hola", 18))
    print(
        "Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: 'Hola <nombre> tienes <edad> años'")
    print(funcion3(2022, 2003, "Cristian"))
'''

##########################################################################################################
# Dia 26 de Agosto de 2022

""" import ops.operaciones as op
import ops.sumar as s           # Alias
import ops.cuadrado as c
from ops.operaciones import multiplicar


if __name__ == "__main__":
    a = 10
    b = 5
    print(s.sumar(a,b))
    print(op.restar(a,b))
    print(op.dividir(a,b))
    print(c.cuadrado(a))
    print(multiplicar(a,b))
 """

###########################################################################################################
 # Dia 31 de Agosto de 2022

'''
n1 = 10
msg = "Hola"
print(n1,msg)
print(str(n1)+msg)
#fstrings
print(f"{n1} {msg}")
'''

""" '''
Hacer una funcion que reciba el nombre de una persona y el año de nacimiento de una persona
el año de nacimiento y el año actual retornando el mensaje "Hola <nombre>, tienes <edad> años"
'''

def funcion1(nombre:str, anoactual:int, anonac:int)->str:       # Funcion que pide un dato de tipo str y dos datos de tipo int
    edad = anoactual - anonac   # Calculamos la edad restando el año actual al año de nacimiento
    return f"Hola <{nombre}>, tienes <{edad}> años"     # Retornamos el valor de una cadena "Hola <nombre>, tienes <edad> años"
    #return f"Hola <{nombre}>, tienes <{anoactual - anonac}> años"  # Retornamos el valor de una cadena "Hola <nombre>, tienes <edad> años"

def funcion2(nombre:str, anoactual:int, anonac:int)->str:       # Funcion que pide un dato de tipo str y dos datos de tipo int
    return f"Hola <{nombre}>, tienes <{anoactual - anonac}> años"  # Retornamos el valor de una cadena "Hola <nombre>, tienes <edad> años"

def calcular_edad( anoactual:int, anonac:int)->int:
    return anoactual-anonac

def funcion3(nombre:str, anoactual:int, anonac:int)->str:
    return f"Hola <{nombre}> tienes <{calcular_edad(anoactual, anonac)}> años"


if __name__ == "__main__":
    print(funcion1("Cristian", 2022, 2003))                 # Imprimimos el resultado del valor retornado de la funcion1
    print(funcion2("Cristian", 2022, 2003))  # Imprimimos el resultado del valor retornado de la funcion2
    res = funcion1("Cristian", 2022, 2003)   # Asignar el valor del valor retornado de la funcion1 a la variable res
    print(res)      # Imprimir el valor de la variable res
    print(funcion3("Cristian", 2022, 2003))
 """

# Listas
""" 
alumnos = ["Hugo", "Paco", "Luis", "Lupita"]        # Crear una lista de alumnos
print(f"Alumnos: {alumnos}")            # Imprimir una lista de alumnos

for i in range(len(alumnos)):               # Crear un ciclo for en un rango de la longitud de la lista alumnos
    print(f"Alumno {i+1}: {alumnos[i]}")        # Imprime cada numero de alumno con su nombre
"""

# Tuplas
""" 
alumnos = ("Hugo", "Paco", "Luis", "Lupita")    # Crear una tupla de alumnos
print(f"Alumnos: {alumnos}")                    #Imprime la tupla de alumnos

for i in range(len(alumnos)):                   # Crear un ciclo for en un rango de la longitud  de la tupla alumnos
    print(f"Alumno {i+1}: {alumnos[i]}")
 """

# Sets
"""
alumnos = {"Hugo", "Paco", "Luis", "Lupita"}
print(f"Alumnos: {alumnos}")
"""

# Diccionarios
"""
alumnos = {"Nombre":"Hugo","Materia1": 10,"Materia2": 5}
print(f"Alumnos: {alumnos}")
print(f"Alumno: {alumnos['Nombre']}")
"""


""" e = ["Nombre", "Est Dat", "Prog Func", "Ingles"]
alumnos = ["Hugo Alberto", "Paco", "Luis", "Lupita"]
materia_e_d = [9,7,9,8]
materia_p_g = [8,9,7,8]
materia_i = [6,7,9,8]

ancho = 15

print(f"{e[0]:^{ancho}} {e[1]:^{ancho}} {e[2]:^{ancho}} {e[3]:^{ancho}}")
for i in range(len(alumnos)):
    print(f"{alumnos[i]:<{ancho}} {materia_e_d[i]:^{ancho}} {materia_p_g[i]:^{ancho}} {materia_i[i]:^{ancho}}")  """

###########################################################################################################################
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
#Dia 07 de Septiembre de 2022
#Cristian Larios ©
'''
lista1 = [1, 2, 3, 4]   # Crear una lista
print(lista1)

lista2 = [1, 3.14, "a", True, [1,2,3], (1, 2, 3), {8, "a", 5.4}]        # Una lista puede contener cualquier tipo de dato
print(lista2)

print(len(lista1))

print(len(lista2))
print(lista2[6])        # Acceder a un elemento de la lista

lista_cal = []
print(lista_cal)
lista_cal.append(5)     # Agregar un elemento al final de la lista
print(lista_cal)   
lista_cal.append(8)
print(lista_cal)
lista_cal.insert(0,6)   # Modificar el elemento del indice 0
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
'''
#Cristian Larios ©
#########################################################################################################################
# Dia 9 de Septiembre de 2022

