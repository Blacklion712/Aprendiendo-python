#Las listas o matrices si pueden ser modificadas
lista = ['Daniel', 'Lyon712', True, 1.85] 
#Las tuple no pueden ser modificadas
tuple = ('Daniel', 'Lyon712', True, 1.85) 

#Esta correcto ya que si se puede ejecutar
lista[3] = "LyonG"

#Esto es incorrecto ya que no se puede ejecutar
#tuple[3] = "LyonG"

#Creando un conjunto (set)

conjunto = {'Daniel', 'Lyon712', True, 1.85, 'Lyon712' }
 
#Los conjuntos pueden ser rescritos pero los elementos no pueden ser modificados (no se pueden llamar datos por el indice)
#(No se pueden tener o no muestra datos duplicados)
#Ejemplo: conjunto[2] = "LyonG" -- No podra ser ejecutado ya que no se pueden modificar los elementos
#En cambio conjunto = {LyonG} -- Esto esta correcto ya que los conjuntos si pueden ser reescritos
# print(conjunto[3]) --> no se puede acceder al elemento

#Creando un diccionario(dict)

diccionario = {
    'nombre' : 'Daniel',
    'apodo' : 'LyonG',
    'Le gusta' : True,
    'estatura' : 1.85,
    'dato duplicado' : 'LyonG'
}
print(diccionario['estatura'])


