#1 profesor
#1 asisitente

#a) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor

participantes = []

#Bucle para solicitar edades
while True:
    nombre = input(f"Hola bienvenido a la clase, porfavor proporcionanos tu nombre: ")
    

   #Sirve para que convierta todas las letras que se ingresen en el input de nombre a minuscula 
    if nombre.lower() == 'salir':
        break
    
    edad = input(f"Ahora {nombre} tu edad porfavor: ")
    
    #Sirve para almacenar posibles errores que podria tener el codigo
    try:
        edad = int(edad)
        participantes.append((nombre, edad)) #Es para poder tener una especie de diccionario y poder ordenarlo
    
    except ValueError:
        print("Porfavor solo ingresa numeros.")
    


#Creando funcion lamda para ordenar los participantes y las edades

participantes.sort(key=lambda x: x[1])

#El mayor es el profesor y el menor es el asistente, Quien es quien?

#verifica que almenos se tengan 2 participantes
if len(participantes) > 2:
    profesor = participantes[-1]
    asistente = participantes[0]


print(f"Los participantes y las edades de tu grupo son: {participantes}")
print(f"El profesor es {profesor[0]} con {profesor[1]} años de edad")
print(f"El asistente es {asistente[0]} con {asistente[1]} años de edad")

    
 