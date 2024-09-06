animales = {"gato", "perro", "loro", "cocodrilo"}
numeros = {1,5,6,4}

#iterando dos Conjuntos del mismo tamaño al mismo tiempo
for numero,animal in zip(numeros,animales):
    print(f"recorriendo Conjunto 1: {numero}")
    print(f"recorriendo Conjunto 2: {animal}")
    
#funcion range
for num in range(10,20):
    print(num)
    
     
#Forma optima de recorrer una Conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")
    
#usando el else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
    
    
#Es exactamente igual que para listas y tuplas