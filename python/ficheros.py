#Escribir y leer ficheros
#MODOS
# w: escritura, crea el fichero si no existe, si existe reemplaza el contenido anterior por el nuevo
# a: escritura, crea el fichero si no existe, si existe agrega el nuevo contenido al final del contenido existente
# r: lectura de ficheros

#crear manejador para crear un archivo HTML
manejador = open('index.html', 'w')
html = '<!DOCTYPE HTML>\n'
html += "<html lang=\"es\">\n"
html += '<head>\n'
html += '<meta charset="utf-8">\n'
html += '<title>Hola Mundo</title>\n'
html += '</head>\n'
html += '<body>\n'
html += '<h1>Hola Mundo</h1>\n'
html += '<p>Archivo HTML creado a través de Python</p>\n'
html += '</body>\n'
html += '</html>\n'
#Escribir el fichero con .write()
manejador.write(html)
manejador.close()
print()
print('*** Archivo HTML creado con éxito ***')
print()
#Leer archivo
print('Leer archivo con la función .read()')
manejador = open('index.html', 'r')
contenido = manejador.read()
print(contenido)
manejador.close()
print()
#Obtener contenido línea a línea
print('Leer el fichero línea a línea a través de un bucle')
manejador = open('index.html', 'r')
for linea in manejador:
    print(linea, end='')
manejador.close()