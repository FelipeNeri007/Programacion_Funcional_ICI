# Unidad I: Tópicos Avanzados de Programación
## Problemas resueltos en clase con Python3
### Ejercicio 1.1. Escribir una funcion que reciba dos argumentos de tipo string e imprima en pantalla "Hola {argumento1} tienes {argumento2} años"
### 1.1 Descripcion del ejercicio
  Se necesita crear una funcion que en sus argumentos los hints sean argumento1 como tipo de dato str y arugmento2 como tipo de dato str y el valor de salida será de tipo string y posteriormente mandarla a llamar introduciendole sus argumentos
#### 1.2 Código
```python
def funcion1(a: str, b: str) -> str:
    return f"<{a}> <{b}>"
```
 #### 1.3 Implementación
 ```python
 print(funcion1("Hola", "Cristian"))
 ```
#### 1.4 Salida
```python
Hola Cristian
```

### Ejercicio 1.2 Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: "Hola {nombre} tienes {edad} años"
#### 1.1 Descripcion del ejercicio
Se necesita crear una funcion que en sus argumentos los hints sean argumento1 como tipo de dato str y arugmento2 como tipo de dato int y el valor de salida será de tipo string y posteriormente mandarla a llamar introduciendole sus argumentos
#### 1.2 Código
```python
def funcion2(a: str, b: int) -> str:  
    return f"Hola {a} tienes {b} años"
```
#### 1.3 Implementación
```python
print(funcion2("Cristian", 18))
```
#### 1.4 Salida
```python
Hola Cristian tienes 18 años
```

### Ejercicio 1.3 Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: "Hola {nombre} tienes {edad} años"
#### 1.1 Descripcion del ejercicio
Se necesita crear una funcion que en sus argumentos los hints sean argumento1 como tipo de dato int, argumento2 como tipo de dato int y argumento3 como tipo de dato str y el valor de salida sea de tipo string, se debe usar la funcion del anterior ejercicio dentro de esta funcion para hacer el proceso.
#### 1.2 Código
```python
def funcion3(a: int, b: int, c: str) -> str:
    edad = a - b
    return funcion2(c, edad)
```
#### 1.3 Implementación
```python
print(funcion3(2022, 2003, "Cristian"))
```
#### 1.4 Salida
```python
Hola Cristian tienes 19 años
```

### Ejercicio 1.4 Importacion de modulos
#### 1.1 Descripcion del ejercicio
Conocer el uso de la importacion de modulos desde otros archivos para tener una presentacion mas limpia y facilitar la lectura del codigo.
#### 1.2 Código
```python
import ops.operaciones as op
import ops.sumar as s
import ops.cuadrado as c
from ops.operaciones import multiplicar
```
#### 1.3 Implementación
```python
a = 10    
b = 5     
print(s.sumar(a,b))  
print(op.restar(a,b))
print(op.dividir(a,b))
print(c.cuadrado(a))
print(multiplicar(a,b))
```
#### 1.4 Salida
```python
15
5
2.0
100
50
```
### Ejercicio 1.5 
#### 1.1 Descripcion del ejercicio
#### 1.2 Código
```python

```
#### 1.3 Implementación
```python

```
#### 1.4 Salida
```python

```

### Ejercicio 1.6
#### 1.1 Descripcion del ejercicio
#### 1.2 Código
```python

```
#### 1.3 Implementación
```python

```
#### 1.4 Salida
```python

```

### Ejercicio 1.7 
### 1.1 Descripcion del ejercicio
### 1.2 Código
```python

```
### 1.3 Implementación
```python

```
### 1.4 Salida
```python

```
