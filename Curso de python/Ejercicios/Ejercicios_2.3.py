#Crea una funcion que muestre la serie fibonacci entre el 0 y el numero dado

def fibonacci(num):
    x,y = 0,1
    Fibonacci_lista = [0]
    while y <= num:
        Fibonacci_lista.append(y)
        x, y = y, x + y
    return Fibonacci_lista
        

Limite = int(input("Dame el numero limite: "))
resultado = fibonacci(Limite)
print(f"Tu lista fibonacci es: {resultado}")

    
