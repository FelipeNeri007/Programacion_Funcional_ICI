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


def funcion1(a: str, b: str) -> str:
    return f"<{a}> <{b}>"


'''
Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: "Hola <nombre> tienes <edad> años
'''


def funcion2(a: str, b: int) -> str:
    return f"Hola {a} tienes {b} años"


'''
Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "Hola <nombre> tienes <edad> años"
'''


def funcion3(a: int, b: int, c: str) -> str:
    edad = a - b
    return funcion2(c, edad)


if __name__ == "__main__":
    print("Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla '<mensaje> <nombre>'")
    print(funcion1("Hola", "Cristian"))
    print(
        "Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: 'Hola <nombre> tienes <edad> años'")
    print(funcion2("Hola", 18))
    print(
        "Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: 'Hola <nombre> tienes <edad> años'")
    print(funcion3(2022, 2003, "Cristian"))
