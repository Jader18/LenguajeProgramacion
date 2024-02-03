

palabra = input("Ingresa una frase/palabra para saber cuantas letras tiene: \n")


count = 0


# Iterar sobre cada caracter en la cadena
for caracter in palabra:
    # Verificar si el caracter es una letra
    if caracter.isalpha():
        # aumentar el conteo si es letra
        count = count + 1

print("Cantidad de letras en la frase/palabra ingresada:", count)
