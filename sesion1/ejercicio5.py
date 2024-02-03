cantidadMoneda = float(input("Ingrese la cantidad con la moneda original: "))
tipoMoneda = input("Ingrese el tipo de moneda original: 'D' - Dolares || 'C' - Cordobas: \n")

tasaCordoba = 0.027
tasaDolar = 36.62

if tipoMoneda == "D": 
    resultado = cantidadMoneda * tasaDolar
    print("$", cantidadMoneda, "equivalen a C$", resultado)

elif tipoMoneda == "C":
    resultado = cantidadMoneda * tasaCordoba
    print("C$", cantidadMoneda, "equivalen a $", resultado)