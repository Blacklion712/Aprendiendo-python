diccionario = {
    "nombre" : 'Juan',
    "apellido" : 'Garcia',
    "subs" : 100000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get
valor_nombre = diccionario.get("nombre")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario)