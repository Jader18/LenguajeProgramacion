
n1 = float(input("Ingrese un numero: "))

n2 = float(input("Ingrese otro numero: "))

print("\n ***Seleccione una operacion: ***")

print("\n 1) Suma \n 2) Resta \n 3) Multiplicacion \n 4) Division ")

opc = int(input("Elige una opcion: "))


if opc == 1:
    print("Suma: ", n1 + n2)

elif opc == 2:
    print("Resta: ", n1 - n2)

elif opc == 3:
    print("Multiplicacion: ", n1 * n2)

elif opc == 4:
    print("Division: ", n1 / n2)

else: 
    print("Opcion invalida")





