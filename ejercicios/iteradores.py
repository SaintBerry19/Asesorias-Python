# import random 
# Iterando con while
# while (condicion de iteracion):
# bloque de codigo
# repeticion
# Recordar que while se ejecutara siempre y cuando la condicion de iteracion se cumpla
# Se utiliza para longitudes desconocidas

# while True:
#     print("hola")
#     break

# Iterando con for
# for elemento_de_iteracion in iterando:
# bloque de codigo
# repeticion
# Recordar que for se va a iterar de acuerdo con la longitud del iterando.
# Se usa para longitudes conocidas o trabajar con listas
# El range del iterando siempre en cero al menos que se especifique lo contrario y es excluyente,
# es decir, no se toma en cuenta su propio valor.
# range(inicio (incluyente), final (excluyente), paso)

# for iterador in range(10):
#     if iterador % 2 == 0:
#         print(f"El iterador es par: {iterador}")
#     else:
#         print(f"El iterador no es par: {iterador}")


# lista= [random.randint(1, 10) for i in range(10)]
# oracion="Hola me llamo diego arciniega perez"
# lista_de_palabras=oracion.split(" ")

# print(f"Lista: {lista}")
# print(f"Oracion: {oracion}")
# print(f"Lista de palabras: {lista_de_palabras}")

# No puedes trabajar con el indice de la lista, solo con el elemento directo, sin embargo esto es mucho mas practico.
# print ("Trabajando con la lista")
# for elemento in lista:
#      print (elemento)
# print ("//////////////////////////////////////////////")

# La ventaja de usar un iterador exerno a la lista, es que puedes trabajar con el indice de la lista y con el elemento de ese indice.
# for iterador in range (len(lista)):
#     print(f"Este es el elemento numero {iterador} de la lista: {lista[iterador]}")
#     print("Este es el elemento numero", iterador, "de la lista:", lista[iterador])

# for indice,elemento in enumerate(lista):
#     print(f"Este es el elemento numero {indice} de la lista: {elemento}")

# Puedes iterar strings
# print ("Trabajando con la oracion")
# for elemento in oracion:
#      print (elemento)
# print ("//////////////////////////////////////////////")

# Puedes iterar listas con palabras u incluso otras listas
# print ("Trabajando con la lista de palabras")
# for elemento in lista_de_palabras:
#      print (elemento)
# print ("//////////////////////////////////////////////")

# try:
#     a = int(input("dime algo: "))
#     a = a/0
# except Exception as e:
#     print("Hubo un error:", e)

# lista=[1,2,3,4,5]

# for i in lista:
#     print(i)

# for i in range(len(lista)):
#     print(lista[i])

# for indice,elemento in enumerate(lista):
#     print(indice, elemento)

# lista_anidada=[[1,2],[3,4],[5,6],[7,8]]

# for lista in lista_anidada:
#     print(lista)

# for calificacion1,calificacion2 in lista_anidada:
#     print(calificacion1,calificacion2)

# for lista in enumerate(lista_anidada):
#     print(lista)

# x=40
# for i in range(0,x,10):
#     print(i)