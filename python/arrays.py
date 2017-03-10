#listas, sus elementos son de lectura y escritura
lista = ['Python', 'Java' ,15 ,'Hola mundo', 3.14]
        #index 0     1     2       3           4  
print(lista[0])
#Cambiar valor en la lista
lista[0] = 'Nuevo valor'
print(lista[0])
#tuples, sus elementos son solo de lectura
tuples = ('Manuel', 'Rosa', 2, 'Hola tuples')
print(tuples[2])
#Tratamiento de listas y tuples
#mostrar todos los valores
print('Todos los elementos de tuples son:',tuples)
print('Todos los elementos de la lista',lista)
#Extraer una parte de los elementos de la lista o del tuples
#extraer desde la posicion index inicial hasta el numero del elemento seleccionado
print(tuples[1:4])
print(lista[2:4])
#extraer desde la posición index indicada hasta el final
print(tuples[2:])
print(lista[1:])
#retornar una lista o tuples varias veces
nuevo_array = tuples * 2
print(nuevo_array)
#Concatenar listas
lista_1 = ['uno', 'dos', 'tres']
lista_2 = ['cuatro', 'cinco', 'seis']
lista_concatenada = lista_1 + lista_2
print(lista_concatenada)
print(lista_concatenada[3])