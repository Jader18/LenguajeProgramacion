#creacion de una lista de numeros pares
#imprimir la lista de los primeros 5 numeros pares

print("Los primeros 5 numeros pares")

def par(num): 
    return num % 2 == 0

cont = 0
numero = 1

while cont < 5:
    if par(numero):
        print(numero)
        cont = cont + 1
    numero = numero + 1

    


