class Persona():
    #metodo constructor
    def __init__(self):
        #propiedades(variables) privadas
        self.__nombre = 'Introduzca un nombre'
        self.__pais = 'Introduzca un pais'
        #propiedad publica
        self.sexo = ['Hombre', 'Mujer']
    #metodos
    def nombre(self, nombre=''):
        if(nombre !=''):
            return nombre
        else:
            return self.__nombre
    def pais(self, pais=''):
        if(pais !=''):
            return pais
        else:
            return self.__pais
    def edad(self, edad=0):
        return edad
    def estatura(self, estatura=0):
        return estatura
    def peso(self, peso=0):
        return peso