#Módulos glob y os
import glob, os.path
#glob permite indexar en la ruta seleccionada para examinar los archivos y documentos que contiene

#path es un submódulo de os, que nos permitirá entre otras cosas saber si un archivo o carperta existe en la ruta indicada

#Mostrar archivos y carpetas de directorio
todos = glob.glob('directorio/*')
print('Todos los archivos y capertas de directorio:', todos)
print()
#Mostrar solo archivos de directorio
archivos = []
for element in todos:
    if(os.path.isfile(element)):
        archivos.append(element)
print('Todos los archivos del directorio:', archivos)
print()
#Extraer las carpetas de directorio
carpetas = []
for element in todos:
    if(os.path.isdir(element)):
        carpetas.append(element)
print('Todas las carpetas de directorio:', carpetas)
print()
#Extraer archivos con por su extensión
txt = glob.glob('directorio/*.txt')
print('Archivos con extensión .txt de directorio', txt)
print()
#Extraer archivos por número de caracteres
txt3char = glob.glob('directorio/???.txt')
print('Archivos con nombre de 3 caracteres en directorio:', txt3char)
