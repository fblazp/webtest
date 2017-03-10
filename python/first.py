#Comentarios, no afectan el código, el interpetre no los lee
#Imprimir mensaje en pantalla
print("Hola Mundo")
#Variables
string = "Hola Mundo String"
print(string)
#cambio de valor
string = "Estoy cambiando de valor"
print(string)
#Crear varias variables
a,b,c = 1, 2, 3
print('Valor de las variables a, b y c',a, b, c) #concatenar
#Eliminar variables con del
del a, b, c
#print(a, b, c)
#tipos de datos y concatenar
string = 'Cadena texto' #tipo texto
integer = 12 #tipo entero
float = 3.1416 #tipo float (con decimales)
#convertir tipo de datos en las variables
#convertir a String str()
concatenar = string +' '+str(integer)+' '+str(float)
print(concatenar)
#convertir un string a interger int()
string ='1'
integer = 1
total = int(string) + integer
print('El total es:', total)