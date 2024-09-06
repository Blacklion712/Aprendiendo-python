#Creando funcion simple
#def saludo():
#    print("Hola daniel, como estas?")


#Ejecutando la funcion simple    
#saludo()

#Funcion que contenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == 'mujer'):
        adjetivo = "reina"
    elif(sexo == 'hombre'):
        adjetivo = "Titan"
    else:
        adjetivo = "amor"
        

    print(f"Hola {nombre}, mi {adjetivo} como estas?")
    
saludar("Daniel", 'Hombre')
saludar("Gabriela", 'MuJer')
saludar("Fred", 'no binario')

#Crear una funcion que me retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
    
pasword = crear_contraseña_random(30)
frase = f"Tu nueva contraseña es {pasword}"
print(frase)


#Crear una funcion que me retorne varios valores
def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña, num
    
pasword, primer_numero = crear_contraseña_random(987)

#monstrado los rersultados obtenidos y los datos utilizador para obtenerlos
print(f"Tu contraseña nueva es: {pasword}")
print(f"El numero utilizado para crearla fue: {primer_numero}")



