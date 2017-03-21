from datetime import date, datetime
#OBJETO DATE
print('Fecha actual:', date.today())
print('Día del mes:', date.today().day)
print('Mes del año:', date.today().month)
print('Año actual:', date.today().year)
print('Día de la semana:', date.today().weekday())

#Dar formato a las fechas
mes ={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}
dia_semana ={0:'lunes',1:'martes',2:'miércoles',3:'jueves',4:'viernes',5:'sábado',6:'domingo'}

fecha = 'Hoy es '+ dia_semana[date.today().weekday()] + ' '+ str(date.today().day) + ' de ' + mes[date.today().month] + ' del ' + str(date.today().year)
print(fecha)
print()
print()
#OBJETO DATETIME
print('Fecha y hora actual:', datetime.now())
print('Microsegundos actuales:', datetime.now().microsecond)
print('Segundos actuales:', datetime.now().second)
print('Minutos actuales:', datetime.now().minute)
print('Hora actual:', datetime.now().hour)

# metodo strftime(string)
#fecha
# %Y año con cuatro digitos
# %m mes con dos digitos
# %d dia con dos digitos
#hora
# %H hora en formato 24h
# %M minutos actuales
# %S segundos actuales
print(datetime.now().strftime('%a-%d-%m-%Y %H:%M:%S'))