#Palabras al Revés:
#Toma tres palabras y muéstralas escritas al revés sin usar sentencias de control.

print("Ingrese una palabra: ")
palabra1 = input()

print("Ingrese una palabra: ")
palabra2 = input()

print("Ingrese una palabra: ")
palabra3 = input()

palabra1_invertida = palabra1[::-1]
palabra2_invertida = palabra2[::-1]
palabra3_invertida = palabra3[::-1]

print("Palabra ingresada: ", palabra1, " || Palabra invertida", palabra1_invertida)
print("Palabra ingresada: ", palabra2, " || Palabra invertida", palabra2_invertida)
print("Palabra ingresada: ", palabra3, " || Palabra invertida", palabra3_invertida)
