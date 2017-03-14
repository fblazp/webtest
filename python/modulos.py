#Modulos
#ejemplo 1 - accediendo a través del namespace
import modules.matematicas
print('Ejemplo 1:', modules.matematicas.sumar(2, 2, 4, 8))
#ejemplo 2 - accediendo a través de un alias
import modules.matematicas as m 
print('Ejemplo 2:', m.restar(10, 5, 10))
#ejemplo 3 - acceder directamente a los elementos sin usar el namespace ni alias
from modules.matematicas import * #importar todos los elementos del modulo
print('Ejemplo 3:', multiplicar(3, 3, 3))
#ejemplo 4 - obtener un determinado elemento del modulo
from modules.matematicas import dividir, sumar
print('Ejemplo 4:', dividir(10, 2))
#ejemplo 5 - asignar un alias a los elementos del modulo
from modules.matematicas import multiplicar as m, sumar as s
print('Ejemplo 5:', m(2, 3, 4))
print('Ejemplo 5.1:', s(1, 2, 3, 4, 5))