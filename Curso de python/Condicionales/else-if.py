Salario_mensual = 15000
Gastos_mensuales = 87000

'''if Salario_mensual >= 20000:
    print('Se le autoriza un credito por $100,000 mxn')
elif Salario_mensual > 15000:
    print('Se le autoriza un prestamo por $50,0000 mxn')
elif Salario_mensual > 10000:
    print('Se le autoriza un prestamo por $25000 mxn')
else:
    print('Su sueldo es muy bajo, no se le puede autorizar ningun prestamo')'''

if Salario_mensual > 13000:
    if Salario_mensual - Gastos_mensuales < 0:
        print("Tienes muchos gastos, te estas quedando pobre")
    elif Salario_mensual - Gastos_mensuales > 4000:
        print("Vas bien tienes una buena gestion financiera")
    else:
        print("Estas dentro del promedio en gastos, mejora.")
elif Salario_mensual > 7000:
    print('Tienes un salario promedio, busca mejorar')
elif Salario_mensual > 3000:
    print("Tienes un salario bajo, busca otro trabajo")
else:
    print("No ganas nada de dinero, busca un trabajo olgasan")