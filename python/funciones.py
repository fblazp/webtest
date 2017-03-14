#Funciones en Python
#función simple
def saludo():
    return 'Hola Mundo'
#Acceder a la función
print(saludo())
#función con un argumento o parámetro
def escribe(string):
    return string
print(escribe('Función con argumentos'))
#función con mas de un parámetro
def multiplicar(num1, num2):
    return num1 * num2
print(multiplicar(2, 5))
#función con parámetro opcional
def sumar(num1, num2=0):
    return num1 + num2
print(sumar(8))
print(sumar(8, 8))
#función con un argumento que es un array
#extraer el index del array
def arrayIndex(arr):
    resultado = ''
    for value in range(len(arr)):
        resultado += str(value)
    return resultado
lista = [0, 'hola', 1.23, 'Python', 3.14]
print(arrayIndex(lista))
#extreaer elementos del array
def arrayElements(arr):
    resultado = ''
    for value in arr:
        resultado += str(value)
    return resultado
lista = [0, 'hola', 1.23, 'Python', 3.14]
print(arrayElements(lista))
#pasar tantos argumentos como necesitemos
def argumentos(*arg):
    for var in arg:
        print(var, end=" ")
argumentos(1, 2, 'Hola', 'Python', 3.14, 'mundo')
print('\n\n***funciones lambda***\n')
#Lambda
#lambda nos permite crear funciones con una sola instrucción
restar = lambda num1, num2: num1 - num2
#llamar a lambda
print(restar(10, 3))