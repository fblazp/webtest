entero = input('Introducir un número entero: ')
#Si el usuario introduce datos de tipo string o float, se producirá un error que detendrá la ejecucción del programa, para evitarlo se usa la estructura try: except:
try:
    entero = int(entero)
    print('El valor', entero, 'es correcto')
#ValueError captura el error y evita que se detenga el programa
except ValueError:
    print('Se ha producido un error, no has ingresado un número entero')