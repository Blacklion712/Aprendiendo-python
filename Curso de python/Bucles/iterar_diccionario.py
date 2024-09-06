diccionario = {
    'nombre' : 'Daniel',
    'apodo' : 'Lyon',
    'subs' : 1000000
}

#Recorriendo el diccionario con .items() para obtener las claves y valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"La clave es: {key} y  el valor es: {value}") 