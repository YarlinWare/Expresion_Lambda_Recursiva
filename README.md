# Ejercicio 4: Implementación Funciones Lambda
### Función Lambda con recursividad [Sucesión de Fibonacci, Factorial]
##### Modelos de programación II - G.020-82

#### Descripción

Se desarrolla ejercicio de implementación de funciones anónimas Lambda con recursiva en python, para resolver la implementación de sucesiones de Fibonacci y El factorial de un numero determinado.


#### Funciones lambda

El operador lambda sirve para crear funciones anónimas en línea. Al ser funciones anónimas, es decir, sin nombre, estas no podrán ser referenciadas más tarde.

Las funciones lambda se construyen mediante el operador lambda, los parámetros de la función separados por comas (atención, SIN parénte-sis), dos puntos (:) y el código de la función.

Ejemplo:
```
#Estructura
# lambda arg1, arg2 :  retorno función anónima

#Ejemplo
nombre_var = lambda a, b: a+b
```

Para el el desarrollo del ejercicio se desarrollo el ejercicio con funciones, implementando recursividad:

```
#Fibonacci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

#Factorial
def factorial(num):
   if num == 0 or num == 1:
      return 1
   else:
      return num * factorial(num - 1)
```

De allí se parte, para ajustar las estructuras de nuestras funciones anónimas:

```
#Estructura
#nombre_var = (lambda funcion: lambda argumento: funcion(funcion,argumento))(función principal)(argumento)

#Fibonacci
fibonacci = (lambda fun: lambda arg: fun(fun,arg)) (lambda f,a:0 if a==0 else (1 if a==1 else f(f,a-1)+f(f,a-2))) (numero)

#Factorial
factorial = (lambda fun: lambda arg: fun(fun,arg)) (lambda f,a: 1 if a ==0 else a*f(f,a-1))(numero)
```


#### Ejecutar proyecto
```
~$ python expresion_lambda.py
```


#### Estructura del proyecto
+ expresion_lambda.py
+ README.md


#### Referencias
[1] `Python para todos - Raúl González Duque`: [PDF](http://www.utic.edu.py/citil/images/Manuales/Python_para_todos.pdf)
[2] `Héctor Costa Guzmán`: [BLOG](https://docs.hektorprofe.net/python/funcionalidades-avanzadas/funciones-lambda/)


#### Equipo de trabajo

Integrante  | Código
------------- | -------------
Cristhian Mauricio Yara Pardo | 20181020081
