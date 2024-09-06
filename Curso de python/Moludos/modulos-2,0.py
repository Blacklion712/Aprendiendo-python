#Si la carpeta estuviera en la misma ruta se importa de esta manera
#import modulos_buenos.saludar as m_saludar

#Si la carpeta no estuviera en la misma ruta, se importaria de esta manera con sys:

import sys

sys.path.append('c:\\Users\\black\\OneDrive\\Documentos\\Curso de python\\modulos_buenos')

import saludar as modulo_saludo

print(modulo_saludo.saludar('Daniel'))