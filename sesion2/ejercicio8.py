#Suma de Dígitos:
#Elige un número de dos dígitos.
#Suma los dígitos individualmente y muestra el resultado

num = 14

#se convierte el numero en string
numString = str(num)

#se separan los digitos
primerDigito = numString[0]
segundoDigito = numString[1]

#se convierten los numeros de string a int 
primerDigito = int(primerDigito)
segundoDigito = int(segundoDigito)

print("El numero entero es: ", num, "|| El primer digito es: ", primerDigito, " | El segundo digito es: ", segundoDigito)
