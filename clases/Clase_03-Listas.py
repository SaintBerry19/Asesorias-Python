# Listas, estructura de datos iterable, esta compuesta de elementos, al igual que los strings es indexable
# el indexing se utiliza para acceder a ellas.
# Las listas son mutables, es decir se puede sobreescribir el valor de sus elementos
# Una lista puede contener mas listas dentro de ella.
# lista = [elemento, otro_elemento, mas_elementos]
# Nota indexacion ( y tambien la funcion range) tienen la estructura de inicio incluyente:final excluyente:salto entre elementos, si alguno esta vacio los defaults son:
# todo, todo, 1
# Indexacion de la lista
lista = [1,2,3,4,5,6]
print(lista[2])
print(lista[-2])
print(lista[0:4:2])
print(lista[0:5:2])
print(lista[::-1])
print(lista[::-2])
print(lista[-4::-1])

# Son iterables
print("")
print("Listas son iterables")
for elemento in lista:
    print(elemento)

# Tambien son mutables:
# Si a la funcion range se le da un valor solamente, el default es ir de 0 a ese valor sin contar el valor de 1 en 1, es decir, 0:valor:1
# Len es una funcion que retorna el tamania o longitud de un objeto iterable.
print("")
print("Listas son mutables")
for iterador in range(len(lista)):
    lista[iterador] = 2 + iterador
print(lista)

# # Listas
# print("")
# print("Uso de IN")
# lista = [1, 2, 3, 4, 5]
# numero = int(input("Dame un numero: "))
# if numero in lista:
#     print("El numero esta dentro de la lista")
# else:
#     print("El numero no esta en la lista, pero se agregara")
#     lista.append(numero)
# print(lista)

# # Usar NOT
# print("")
# print("Uso de NOT")
# numero = int(input("Dame un numero: "))
# if numero not in lista:
#     print("El numero no esta dentro de la lista, pero se agregara")
#     lista.append(numero)
# else:
#     print("El numero esta en la lista")
# print(lista)

# # Uso de AND y OR
# print("")
# print("Uso de and y or:")
# lista_inicial = [1, 2, 3, 4, 5]
# if numero in lista_inicial and nombre == "Amaya":
#     print("El numero esta en la lista inicial y se llama Amaya")
# elif numero in lista_inicial or nombre == "Amaya":
#     print("O el numero esta en la lista inicial o el se llama Amaya")
# else:
#     print("No es Amaya y el numero no esta en lista")

# Metodo Index
# .index(valor_a_buscar) ---> regresa el indice del elemento que haga match con el valor, el primero.