animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [1,5,6,4]

#Recoriendo la lista animales
#for animal in animales:
    #print(f"Ahora la variable animal es {animal}")
    
#for numero in numeros:
    #resultado = numero*10
    #print(resultado)
    
    
#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(numeros,animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#funcion range
for num in range(10,20):
    print(num)
    
#Forma no optima de recorrer una lista
#for num in range(len(numeros)):
     #print(numeros(num))
     
#Forma optima de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
    
#usando el else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
