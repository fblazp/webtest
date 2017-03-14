#importar modulo
from modules.persona import Persona
#crear la instancia
persona = Persona()
print('\n\n ---Persona---\n')
print('Nombre:', persona.nombre('Paco'))
print('Pais:', persona.pais('Mamblas'))
print('Edad:', persona.edad(321654))
print('Sexo:', persona.sexo[1])