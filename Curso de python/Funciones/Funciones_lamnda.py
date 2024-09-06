numeros = [1,2,3,4,5,6,7,8,9]


#Creando una funcion lambda para multiplicar por2
nombre = lambda x : x*2

#creando una funcion comun que diga si es par oh no
#def es_par(num):
    #if (num%2==0):
        #return True
    
#Usando filtrar en una funcion comun
#numeros_pares = filter(es_par,numeros)


#creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda numero: numero%2 == 0,numeros)

print(list(numeros_pares))