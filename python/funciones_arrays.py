#len(array) regresa el número de elementos en listas, tuples y diccionarios
diccionario = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
print('Número de elementos del diccionario:', len(diccionario))
#append(valor) agrega un nuevo elemento al final de un array list
lista = ['uno', 'dos', 'tres', 'cuatro']
lista.append('cinco')
print('Nuevo elemento al final de la lista', lista)
#insert(x, valor) inserta el valor antes de la posición dada, solo funciona en listas
lista = ['Python', 'Java', 'Perl']
lista.insert(0, 'C++')
print('Nuevo elemento añadido a la lista:', lista)
#pop(x) Eliminar del array el elemento a través del index x indicado, solo funciona en listas
lista.pop(3)
print('Eliminar elementos de la lista:', lista)
#index(valor) busca el valor indicado en los arrays list o tuples y regresa el index de la primera ocurrencia encontrada, buscando desde el principio hasta el final
tuples = ('HTML', 'CSS', 'JavaScript', 'PHP', 'HTML', 'PHP', 'JavaScript')
print('Primera posición index del valor seleccionado', tuples.index('PHP'))
#remove(valor) busca la primera ocurrencia del valor dado y lo elimina, solo valido para listas
lista = ['España', 'Francia', 'Italia', 'Austria', 'EEUU']
lista.remove('EEUU')
print('Eliminar elementos de la lista:', lista)
#count(valor) busca el numero de veces que aparece el valor dado en los list y tuples
tuples = ('uno', 'dos', 'tres', 'dos')
print('Número de veces que se repite un elemento:', tuples.count('dos'))