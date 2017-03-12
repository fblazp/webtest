#diccionarios, se accede a ellos a través de una clave asignada
diccionario = {'1': 'Python', '2': 'Java', 3: 'PHP','otro': 'C++'}
#acceder al diccionario
print(diccionario[3])
print(diccionario['2'])
print(diccionario['otro'])
#mostrar claves del diccionario .keys()
print("Las claves del diccionario son:", diccionario.keys())
#extraer los valores del diccionario .values()
print("Los valores del diccionario son:", diccionario.values())
#extraer el diccionario completo
print("El diccionario completo es:", diccionario)