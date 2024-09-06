#Creando una lista con list
lista = list(["Daniel", "Hola", 26])

#len devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#append agrega un valor a la lista
lista.append("Maravillosa jugada")

#instert agrega un elemento a un indice especifico en la lista
lista.insert(2, "Soy gamer")

#extend agrega varios elementos a la lista
lista.extend({"Varios", 22})

#pop elimina un elemento de la lista
lista.pop(0) #-1 para eliminar el ultimo elemento -2 para el penultimo y asi sucesivamente.

#remove remueve un elemento de la lista por su valor
lista.remove("Maravillosa jugada")

#clear elimina todos los elemento de la lista
#lista.clear()

#sort ordena los elementos de la lista, pero solo valores numeros o true y false en orden acendente
#lista.sort()
#lista.sort(reverse=True) Esto sirve para invertir la lista

#reverse invierte los elementos de una lista
lista.reverse()

#index verifica si un elemento se encuentra en la lista
elemento_encontrado = lista.index(22)

print(cantidad_elementos)