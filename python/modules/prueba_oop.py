class Prueba():
    def __init__(self):
        self.__text = 'Saludo no configurado'
        self.__error = 'Ha ocurrido un error'
    def saludo(self, saludo=''):
        if(saludo !=''):
            return saludo
        else:
            return self.__text
    def calculo(self, x, y):
        total = int(x + y)
        return total