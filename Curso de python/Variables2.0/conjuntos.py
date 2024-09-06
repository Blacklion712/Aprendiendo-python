#Creando un conjunto con set

conjunto = set(["Dato 1", "Dato2"])

#Metiendo conjunto dentro de otro conjunto
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "Dato 4"}

#Teoria de conjuntos

conjunto3 = {1,4,5,8,7}
conjunto4= {1,4,8,9}

#verificando si es un subconjunto
resultado = conjunto4.issubset(conjunto3)
resultado = conjunto4 <= conjunto3

#para verificar que sea un superconjunto
resultado = conjunto4.issuperset(conjunto3)
resultado = conjunto4 >= conjunto3

#verificar si algun numero en comun
resultado = conjunto4.isdisjoint(conjunto3)

print(resultado)