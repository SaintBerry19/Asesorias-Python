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
    lista[iterador] = 2
print(lista)
