#Forma no optima de sumar valores

#def suma(lista):
#    numeros_saumados = 0
#    for numero in lista:
#        numeros_saumados = numeros_saumados + numero
#    return numeros_saumados

#resultado = suma({1,2,34,5,45,46,56,4,3,22,32})


#Forma optima de sumar valores

#Utilizando el operador * como argumento (*args)
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([1,2,34,5,45,46,56,4,3,22,32])






print(resultado2)