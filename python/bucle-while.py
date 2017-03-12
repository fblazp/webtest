#While: el bucle se ejecuta mientras la condición sea cierta
inicio = 0
final = 10
while(inicio<final):
    print(inicio)
    inicio +=1
#en Pyton se puede incluir else en los bucles
else:
    print(final,'**** Valor fuera de rango')
#parar un bucle en un punto determinado con break
start = 0
end = 10
while(start<end):
    print(start)
    if(start==5):
        break
    start +=1
#Recorrer elementos de un array
#len() calcula los elementos que hay en una lista
index = 0
lista = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
while(index<len(lista)):
    print(lista[index])
    index +=1