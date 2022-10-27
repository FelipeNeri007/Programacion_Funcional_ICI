# Unidad II: Programación Orientada a Objetos
## Problemas resueltos en clase con Dart
### Ejercicio 1.1. Crear una lista e iterarla imprimiendo cada dato con su indice.
### 1.1 Descripcion del ejercicio
  Se necesita crear una lista para posteriormente iterarla con un ciclo for imprimiendo cada dato con su indice en el arreglo.
#### 1.2 Código
```dart
void main(List<String> args) {
  final miLista = const [1, 2, 3, 4]; // avoid side effects
  print(miLista);
  }
```
 #### 1.3 Implementación
 ```dart
  for (var i = 0; i < miLista.length; i++) {
    stdout.write("$i: ${miLista[i]} | ");
 ```
#### 1.4 Salida
```
[1, 2, 3, 4]
0: 1 | 1: 2 | 2: 3 | 3: 4 | 
```

### Ejercicio 1.2. calculadora que lea dos numeros del teclado y obtenga suma, resta, multiplicación y division, usando funciones y asingnado valores a dos variables
### 1.1 Descripcion del ejercicio
  Se necesita crear una funcion que indique operacion se va a realizar (suma, resta, multiplicacion o división) y crear varias funciones para hacer la operacion ingresada por el usuario. 
#### 1.2 Código
```dart
String leerDatos(String mensaje) {
  print(mensaje);
  String data = (stdin.readLineSync()!);
  return data;
}

String calculadora(String op, int n1, int n2) {
  if (op == "+") {
    return "$n1 + $n2 = ${suma(n1, n2)}";
  } else if (op == "-") {
    return "$n1 - $n2 = ${resta(n1, n2)}";
  } else if (op == "*") {
    return "$n1 * $n2 = ${multi(n1, n2)}";
  } else if (op == "/") {
    return "$n1 / $n2 = ${divi(n1, n2)}";
  } else {
    return "Operación inválida";
  }
}

int suma(int num1, int num2) => num1 + num2;
int resta(int num1, int num2) => num1 - num2;
int multi(int num1, int num2) => num1 * num2;
int divi(int num1, int num2) => num1 ~/ num2;
```
 #### 1.3 Implementación
 ```dart
 import 'dart:io';
void main() {
  String op = leerDatos("Indica la operación [+,-,*,/]");
  int num1 = int.parse(leerDatos("Dame el primer número"));
  int num2 = int.parse(leerDatos("Dame el segundo número"));
  print("${calculadora(op, num1, num2)}");
}
 ```
#### 1.4 Salida
```
Indica la operación [+,-,*,/]
+
Dame el primer número
3
Dame el segundo número
4
3 + 4 = 7
```

### Ejercicio 1.3
### 1.1 Descripcion del ejercicio
  
#### 1.2 Código
```dart

```
 #### 1.3 Implementación
 ```dart
 
 ```
#### 1.4 Salida
```

```

### Ejercicio 1.4
### 1.1 Descripcion del ejercicio
  
#### 1.2 Código
```dart

```
 #### 1.3 Implementación
 ```dart
 
 ```
#### 1.4 Salida
```

```

### Ejercicio 1.5
### 1.1 Descripcion del ejercicio
  
#### 1.2 Código
```dart

```
 #### 1.3 Implementación
 ```dart
 
 ```
#### 1.4 Salida
```

```

### Ejercicio 1.6
### 1.1 Descripcion del ejercicio
  
#### 1.2 Código
```dart

```
 #### 1.3 Implementación
 ```dart
 
 ```
#### 1.4 Salida
```

```
