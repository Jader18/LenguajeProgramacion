import random

numAle = random.randint(1, 100)

print("***Adivina el numero***")

while True:
    num = int(input("Ingresa un numero - Rango (1-100): \n"))

    if num == numAle:
        print("Has adivinado el numero! La respuesta es: ", num)
        break
    elif num < numAle:
        print("El numero es mayor. Intenta de nuevo. \n")
    else:
        print("El numero es menor. Intenta de nuevo. \n")
