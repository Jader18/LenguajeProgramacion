num = input("Ingresa un numero entero (2 o mas digitos): \n")

sum = 0
for digito in num:

    sum = sum + int(digito) 
   
print("La suma de los digitos del numero ingresado es de: ", sum)