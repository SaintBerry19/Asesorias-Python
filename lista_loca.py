lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = [7,8,9]
matriz = [lista_1,lista_2,lista_3]
# print(matriz)
# for i in matriz:
#     print(i)
# print(matriz[2][0])
# print(lista_1[1]*lista_2[2])

for lista in matriz:
    for index in range(len(lista)):
        if lista[index] == 8:
            lista[index] = 69

print(matriz)
