#Bucle for
#Función para incluir un rango: range(inicio, final)
for x in range(0 ,10):
    print(x)
#Recorrer elementos de un array tuples
provincias = ('Salamanca', 'Zaragoza', 'Badajoz', 'Alicante')
for index in range(len(provincias)):
    print(provincias[index])
#se pueden incluir condiciones dentro de la estructura de for
else:
    print('No existen mas registros')
#el bucle for es muy util para recorrer los elementos de un diccionario
diccionario = {1:'PHP', 2:'Python', 3:'Java', 4:'C++'}
#.items() Obtiene tanto la clave como el valor de cada elemento del diccionario
for clave, valor in diccionario.items():
    print(clave,' :', valor)