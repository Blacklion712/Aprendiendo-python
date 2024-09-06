frutas= ['manzana', 'platano', 'pera', 'guayaba', 'melon', 'naranja', 'fresa', ' durazno']
cadena = "Hola lyon"
numeros = [1,6,7,5,4]

#Usar la condicional continue para continuar el bucle
for fruta in frutas:
    if fruta == 'melon':
        continue
    print(f"Me voy a comer una {fruta}")
    
#utilizr el brake para terminar el bucle
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == 'naranja':
        break
else:
    print("Terminado")
    
#Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#For en una sola linea de codigo(duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)