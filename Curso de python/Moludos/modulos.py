#Importando un modulo y asigandodle un nombre
#import modulo_saludar as m_saludo

#Cambiando el nombre de una funcion cuando tenemos mas de una
#from modulo_saludar import saludar as saludar_normal, saludar_raro as saludar_como_Lyon

#Importando todas las funciones de un modulo
#from modulo_saludar import *


#De un modulo importando una o varias funciones especificas.
from modulo_saludar import saludar, saludar_raro

saludo = saludar("Daniel")
saludo_raro = saludar_raro("Benjamin")

print(saludo)
print(saludo_raro)