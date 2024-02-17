#listas

lista = [1, 2, 3, "manzana", 15.6, True]

print(lista)


#tamaño de la lista
tam = len(lista)
print("El tamaño de la lista es: ", tam)

#imprimir elemento de la lista
print(lista[0])

#imprimir ultimo elemento de la lista
print(lista[tam-1])

#imprimir los primeros 3 elementos
print(lista[0:3])

#imprimir elementos del 4 al 6 
print(lista[3:7])

#agregar un elemento a la lista
lista.append("Jader")

#imprimir los ultimos 3 elementos de la lista
final = len(lista)
inicio = final - 3
print(lista[inicio : final + 1])

#eliminar elementos
lista.remove("manzana")
lista.remove("Jader")

#ordenar lista
lista.sort()
print(lista)


