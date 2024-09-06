cadena1 = 'Hola soy lyon'
cadena2 = 'Estoy programando en python'

#Estructura de las cadaneas
#resultado = DATO.METODO()

#Funciones(Son solo algunas):
#upper - convierte a mayusuclas
mayusc = cadena1.upper()

#lower - convierte todo a minusnculas
minusc = cadena1.lower()

#capitalize - Primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

#find - metodo encuentra la primera aparicion del valor especificado, si no devuelve 1
busqueda_find = cadena1.find('H')

#index - metodo encuentra la primera aparicion del valor especificado, si no devuelve una exepcion(encuentra una cadena dentro de otra cadena)
busqueda_index = cadena1.index('o')
#isnumeric - si es numerico devuelve true
es_numeric = cadena1.isalnum()

#isaplha -  si es alpha numerico devuelve true
is_aplhanum = cadena1.isalpha()

#count - devuelve el numero de coincidencias de una subcadena en la cadena dada
contar_coincidencias = cadena1.count()

#len cuenta los caracteres de una cadena
contar_caracteres = len(cadena1)

#startswith - verifica si una cadena comienza con
empieza_con = cadena1.startswith()

#endswith - verifica si una cadena termina con
termina_con = cadena1.endswith()

#replace - remplaza un pedazo de la cadena por otro dado.
rempaza_un_valor = cadena1.replace(',',' ')

#split -  separa por con el parametro que de demos
cadea_separada = cadena1.split(',')
