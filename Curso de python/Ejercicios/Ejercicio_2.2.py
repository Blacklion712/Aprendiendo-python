#Creando una funcion de nos duevuelva los numeros primos
#entre el 0 y el numero que le pasemos



def es_primo(n):
    #Determinar si un numero es primo
    if n <= 1:
        return False #Si es menor o igual a 1 denendra el bucle
    for i in range(2, int(n**0.5) + 1): #se revisa si n es divisible por algún número entre 2 y la raíz 
        if n % i == 0: #si es divisible por algun numero se termina el bucle.
            return False
    return True

def obtener_primos(hasta):
    #oibtiene todos los numeros primos desde 0 hasta el valor dado
    primos = []
    for num in range(2, hasta + 1): #Verificamos si el valor es primo
        if es_primo(num):
            primos.append(num) #En caso de que si lo agregamos a la lista
    return primos

#Imprimir los primos en consola

lista = int(input(f"Porfavor ingresa el numero hasta el que deseas conocer los numeros primos: "))
primos = obtener_primos(lista)
print(f"Los numeros primos son: {primos}")
    

