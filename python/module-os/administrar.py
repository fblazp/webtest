import os
def init():
    print('**Administrar archivos y carpetas**')
    opcion = input('Selecciona una opción: c=crear y e=eliminar: ')
    if(opcion == 'c'):
        ruta = input('Indica la ruta, si no se indica será la actual: ')
        if(ruta == ''):
            ruta = os.getcwd() + '/'
        #Comprobar si la ruta existe
        if(os.path.isdir(ruta)):
            tipo = input('Indica el tipo a=archivo y c=carpeta: ')
            if(tipo == 'a'):
                archivo = input('Indica el nombre del archivo: ')
                #Crear el archivo en la ruta indicada
                manejador = open(ruta+archivo, 'w')
                manejador.close()
                print('Archivo', archivo, 'creado con éxito')
            elif(tipo == 'c'):
                carpeta = input('Indica el nombre de la carpeta: ')
                #Crear la carpeta
                os.mkdir(ruta+carpeta)
                print('Carpeta',carpeta, 'creada con éxito')
            else: init() #Reiniciar el programa
    elif(opcion == 'e'):
        ruta = input('Indica la ruta, si no se indica será la actual: ')
        if(ruta == ''):
            ruta = os.getcwd() + '/'
        eliminar = input('Indica el nombre del archivo o carpeta a eliminar: ')
        #Si es un archivo
        if(os.path.isfile(ruta+eliminar)):
            os.remove(ruta+eliminar)
            print('Archivo', eliminar, 'eliminado con éxito')
        #Si es una carpeta
        elif(os.path.isdir(ruta+eliminar)):
            os.rmdir(ruta+eliminar)
            print('Carpeta', eliminar, 'eliminada con éxito')
        else:
            init() #Reiniciar el programa
    else:
        init() #Reiniciar el programa
#Llamar a la función
init()