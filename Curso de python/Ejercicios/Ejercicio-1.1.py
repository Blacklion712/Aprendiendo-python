
#Promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos(video sin editar)
crudo_promedio = 5
crudi_dalto = 3.5

#Calculando el tiempo vacio
tiempo_vacio = ((crudo_promedio - otros_cursos_promedio) / crudo_promedio * 100)
tiempo_vacio_dalto = ((crudi_dalto - dalto_curso) / crudi_dalto * 100)

print(f'Un curso promedio elimina un {tiempo_vacio:.2f}% del tiempo vacio')
print(f'Un curso promedio elimina un {tiempo_vacio_dalto:.2f}% del tiempo vacio')

print("----------------------------------")


#Diferencias de duracion

diferencia_con_min = ((otros_cursos_min - dalto_curso) / otros_cursos_min * 100)
diferencia_con_max = ((otros_cursos_max - dalto_curso) / otros_cursos_max * 100)
diferencia_con_promedio = ((otros_cursos_promedio - dalto_curso) / otros_cursos_promedio * 100)

print(f"El curso de dalto dura un {diferencia_con_min}% menos que el mas rapido, ademas que dura un {diferencia_con_max}% menos que el mas lento, esto quiere decir que dura un {diferencia_con_promedio}% menos que el promedio ") 

print("----------------------------------")

#Mostrando la diferencia si los cursos duraran 10 horas
print(f"Ver 10 horas del cuerso de dalto equivale a ver {round(otros_cursos_promedio / dalto_curso)} horas de otros curos")

print("----------------------------------")

#nota: para redondear a 2 decimales, puedes usar round o formato de cadenas.