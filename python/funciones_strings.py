#Convertir la primera letra en mayúscula .capitalize()
string = 'mi primera aplicación'
print('Función capitalize:', string.capitalize())
#Convertir toda la cadena de texto en minúscula .lower()
string = 'HOLA MUNDO'
print('Función lower', string.lower())
#Convertir toda la cadena de texto en mayúscula .upper()
string = 'cadena de texto para convertir'
print('Función upper', string.upper())
#Obtener la longitud de un string len()
string = 'cinco'
print('Función len:', len(string))
#Convertir un string en una lista a través del separador indicado .split()
string = 'uno dos tres cuatro cinco seis'
print('Función split', string.split(' '))
#Reemplazar subcadenas de texto .replace(old, new, max)
string = 'test test test test'
print('Función replace:', string.replace('test', 'hola', 2))
#Contar el número de veces que aparece una subcadena .count()
string = 'hola de nuevo hola'
print('Función count:', string.count('hola', 0, len(string)))
#Eliminar los caracteres del principio de un string .lstrip()
string = '+++++++++++++ usando Python'
print('Función lstrip:', string.lstrip('+'))
#Eliminar los caracteres del final de un string .rstrip()
string = 'Python es el mejor --------------------'
print('Función rstrip:', string.rstrip('-'))
#Posición index de la primera posición de una subcadena de izquierda a derecha .find()
string = 'Hola mundo Python'
print('Función find:', string.find('mundo', 0, len(string)))
#Posición index de la primera posición de una subcadena de derecha a izquierda .rfind()
string = 'Hola mundo mundo Python'
print('Función rfind:', string.rfind('mundo', 0, len(string)))
#Comprobar si los caracteres de un string son digitos numéricos .isdigit(), retorna true o false
string = '65464165'
if(string.isdigit()):
    print('El string', string, 'contiene digitos')
else:
    print('El string', string, 'no contiene digitos')
#Convertir un array en un string a través del separador indicado .join()
separador = '-'
lista = ['uno', 'dos', 'tres', 'cuatro']
print('Función join:', separador.join(lista))