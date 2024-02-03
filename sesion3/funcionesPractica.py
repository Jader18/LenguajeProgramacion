#funciones

#libreria para limpiar consola 
import os
os.system("cls || clear")

def get_full_name(name, last_name):
    full_name = name + ' ' + last_name
    return full_name

#forma 1 para imprimir
print("Hola ", get_full_name("jader", "mendoza"))

#forma 2 para imprimir
print(f"Hola {get_full_name('jader', 'mendoza')}")

