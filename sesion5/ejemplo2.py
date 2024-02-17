def fibonacci(n): 
    if n <= 1:
        return n
    else: 
        return fibonacci (n-1) + fibonacci(n-2)



numeroTerminos = int(input("Digite un numero: "))
print("Serie de Fibonacci: ")
for i in range(numeroTerminos):
    print(fibonacci(i))


