#importar modulo sys
import sys
#Mostrar los argumentos pasados por consolas con .argv, el primer argumento siempre va a ser el nombre del script
print('Todos los argumentos pasados en la linea de comandos:', sys.argv)
print('script ejecutado:', sys.argv[0])
#Multiplicar dos números a traves de la linea de comando
print('\n\n****Programa para multiplicar dos números***\n\n')
numero1 = sys.argv[1]
numero2 = sys.argv[2]
try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    total = numero1 * numero2
    print('El total de la multiplicación es:', total)
except ValueError:
    print('Error: los datos no son del tipo correcto')