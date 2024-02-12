# lista = [1,2,6,7,7,7,7,7,7,8,9]
# lista_2 = [1,2,3,4,5,6,7]

# diccionario = {i: lista.count(i) for i in lista if i in lista_2}
# lista_3 = [i for i in diccionario]
# print(lista_3)

# lista=[]
# lista_nueva=[10]
# print(lista+lista_nueva)
# lista.append(lista_nueva)

# len(lista)

lista=[]
for i in range(10):
    lista.append(i)
lista_2=[_ for _ in range(10)]
print(lista,lista_2)

tablero = [[_ for _ in range(3)] for _ in range(3)]
print(tablero)
lista_vacia=[tablero[i][i] for i in range(3)]
print(lista_vacia)
