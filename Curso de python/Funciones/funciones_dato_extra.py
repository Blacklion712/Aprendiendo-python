#Creando funcion de 3 parametros

#def frase(nombre,apellido,adjetivo):
#    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#Utilizando kayword  arguments
#frase_resultante = frase(adetivo = 'capo', nombre = 'daniel', apellido = 'Garcia')

#Creando la misma funcion con un parametro opcional y un valor por defrecto
def frase(nombre,apellido,adjetivo = "super"):
    return f"Hola {nombre} {apellido}, eres {adjetivo}"
frase_resultante = frase("Daniel", "Garcia")
print(frase_resultante)