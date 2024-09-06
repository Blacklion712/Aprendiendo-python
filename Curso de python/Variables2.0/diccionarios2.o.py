#creando diccionarios con dict()
diccionario = dict(nombre = 'Danie', apodo = 'Lyon')

#Las listas no pueden ser claves, porque son mutables y usamos frozensett para crear conjuntos
diccionario2 = {frozenset(["Daniel", "Lyon"]): "Hola"}

#creando diccionarios con fromkeys(), calor por defecto none
diccionario3 = dict.fromkeys(["nombre", "apodo"])

#creando diccionarios con fromkeys(), cambiando el valor por no se
diccionario4 = dict.fromkeys(["nombre", "apodo"], "no se")

print(diccionario4)