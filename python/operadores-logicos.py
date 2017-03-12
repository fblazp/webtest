#Operadores logicos
#and: las dos condiciones son ciertas
#or: al menos una condicion es cierta
#not: la condicion no es cierta
variable1= 2
variable2= 2
variable3= 3
variable4= 4
#comparar con sentencia if/else
if(variable1==2 and variable3 < variable4):
    print('La condición se cumple')
else:
    print('La condición no se cumple')
    
if not(variable1==2 and variable3 < variable4):
    print('La condición se cumple')
else:
    print('La condición no se cumple')
    
#Operador membership nos va a permitir comprobar listas, duples y strings
#in: el valor es encontrado
#not in: el valor no es encontrado
lista = ['uno', 'dos', 'tres']
if('doss' in lista):
    print('dos se encuentra en la lista')
else:
    print('El index no se encuentra')