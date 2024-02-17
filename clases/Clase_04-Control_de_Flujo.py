# Control de Flujo

# Las funciones de iteracion sirven para controlar el flujo de nuestro codigo, los mas utilizados son:
# - while: esta funcion nos permite continuar iterando mientras se cumpla una condicion en especifico
# Estructura: while (condicion):
#               codigo que se va a repetir
# Ejemplo:
print("Primer Ejemplo: ")
iterador = 10
while iterador != 0:
    print(iterador)
    iterador -= 1
print("a ya vale 0!")

# La ventaja de while es que se puede iterar de manera indefinida hasta que nosotros le demos la instruccion de terminar, utilizando la funcion break:
# Ejemplo:
print("")
print("")
print("Segundo Ejemplo: ")
contador = 0
lista = []
while True:
    print("Esta iteracion solo terminara si el contador es 10")
    contador += 1
    lista.append(contador)
    if contador == 10:
        break
print("Contador ya es 10 y ya tenemos generada nuestra lista!")
print(lista)

# Podemos jugar con la condicion de iteracion de muchas maneras otro ejemplo es el siguiente:
print("")
print("")
print("Tercer Ejemplo: ")
lista = []
contador = 0
while len(lista) < 10:
    lista.append(contador)
    contador += 1
print(lista)
# Existe una funcion llamada continue que permite "brincar" una parte del codigo si asi se desea:
print("")
print("")
print("Cuarto Ejemplo: ")
iterador = -1
while True:
    iterador += 1
    if iterador== 2:
        print("iterador = 2")
        continue # repetiras el proceso pero te saltaras lo que esta abajo del codigo
    elif iterador ==3:
        print("iterador = 3, se imprimira de nuevo el 3 porque no tenemos un continue")
    elif iterador == 5:
        break # rompe la iteracion
    print (iterador)

# Como conclusion podemos decir que while se utiliza cuando tenemos una condicion especifica a cumplir o cuando no sabemos "cuanto" debo de iterar. 
# Por otro lado cuando tenemos un objeto iterable definido, o sabemos "cuanto" debemos iterar, solemos utilizar for
# - for sigue la siguiente estructura:
# for iterador in range(inicio_incluyente,final_excluyente,salto): - Cabe mencionar que si solo le damos un numero a la funcion range 
# el default lo tomara de la siguiente manera (0,n,1)  
print("")
print("")
print("Ejemplo For : ")
for i in range(0,11,2):
    print(i)
print("")
print("")
print("Segundo ejemplo : ")
for i in range(10):
    print(i)
print("")
print("")
lista=[10,20,30,40,50,60,70,80,90,100]
print("Tercer ejemplo : ")
for i in range(len(lista)):
    print(lista[i])
# for como se menciono previamente puede trabjar directamente con objetos iterables(que se puedan indexar), como listas o cadenas, y la forma 
# de utilizarlo es la siguiente:
# for elemento_del_iterable in objeto_iterable:
print("")
print("")
print("Ejemplo de elemento de objeto iterable : ")
for elemento in lista:
    print(elemento)

# Como te puedes dar cuenta los ultimos dos ejemplos representan lo mismo sin embargo cada uno tiene sus ventajas, el primero permite hacer operaciones y modificaciones
# a la lista, ya que se utiliza el iterador para hacer referencia al objeto, mientras que el segundo solo toma el elemento del objeto como un valor aparte,
# esto no nos permite modificar el valor del elemento pero si trabajar con el para realizar mas operaciones de manera mas directa.
print("")
print("")
print("Ejemplo comparativo de ambos metodos: ") 
for i in range(len(lista)):
    lista[i] += 10
print(lista)
lista=[10,20,30,40,50,60,70,80,90,100]
for elemento in lista:
    elemento += 10
print(lista)

# Existe un tercer metodo que nos permite utilizar lo mejor de ambos metodos pasados, este metodo utiliza la funcion enumerate y se escribe de la siguiente manera:
print("")
print("")
print("Ejemplo utilizando enumerate: ") 
lista = [10,20,30,40,50]
for index,elemento in enumerate(lista):
    print(index,elemento)
# Esto nos da la flexibilidad de trabajar con ambos valores:
for index,elemento in enumerate(lista):
    lista[index] = elemento * 10
print(lista)