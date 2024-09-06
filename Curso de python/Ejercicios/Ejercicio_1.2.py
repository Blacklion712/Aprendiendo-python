nombre = input("Hola bienvenido al calculador de velocidad al hablar, cual es tu nombre?: ")

print(f"Hola {nombre}, a continuadion te hare una serie de preguntas para determinar tu velocidad al leer")

frase = input("Cual es el texto que quieres leer?: ")

Dividir_palabras = frase.split(" ")

numero_palabras = len(Dividir_palabras)

palabras_por_minuto = input("cuantas palabras lees por minuto?: ")
numero_palabras_minuto = int(palabras_por_minuto)

Tiempo_lectura = numero_palabras / numero_palabras_minuto

print(f"Te tomaria {round(Tiempo_lectura,2)} minutos leer este texto")
print(f"Dijiste {numero_palabras} palabras al leer el texto")

if Tiempo_lectura > 1:
    print("para flaco tampoco te pedi un testamento")
else:
    print("Genial bro tienes buena velocidad de lectura, ahora te compararemos con dalto")
    
Velocidad_dalto = Tiempo_lectura * 0.30
velocidad_dalto_real = Tiempo_lectura - Velocidad_dalto

print(f"Dalto tardaria en leer esta misma frase {round(velocidad_dalto_real,2)} minutos")

