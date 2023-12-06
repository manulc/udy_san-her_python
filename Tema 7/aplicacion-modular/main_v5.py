from mipaquete import *

"""Esta sentencia es para distinguir si un archivo de Python se está ejecutando directamente o si se
está importando en otro archivo de Python como un módulo.
La variable "__name__" es una variable global de Python que indica el nombre del módulo.
Si el archivo de Python se ejecuta directamente, el valor de esta variable será "__main__". Sin embargo,
si el archivo de Python se importa en otro archivo, el valor de esta varible será el nombre del módulo."""
if __name__ == '__main__':
    mimodulo.func_mimodulo()
    mimodulo2.func_mimodulo2()