# Tabla de Veradad
# OR
print(True or False)
print(True or True)
print(False or False)

# AND
print(True and False)
print(True and True)
print(False and False)

# Condiocionales
# IF, ELIF, ELSE , se utilizan para hacer una comparacion y generar una condicion de cumplimiento.
# Tiene la estrucutra IF condicion:  (SI ESTO)
#                           entonces
#                     ELIF condicion: (SI ESTO OTRO)
#                           entonces
#                     ELSE: (SI NINGUNA DE LAS ANTERIORES)
#                           entonces
# Los operados condicionales/logicos son los siguientes, ==,<=,>=,!=,NOT, AND, OR, IN.
print("")
print("Uso de condicionales")
nombre = input("Dime tu nombre: ")
oracion = f"Hola me llamo {nombre}"

if oracion == "Hola me llamo Amaya":
    print("Se llama Amaya")
elif oracion == "Hola me llamo Roberto":
    print("Se llama Roberto")
else:
    print("No es ni Amaya ni Roberto")

# Listas
print("")
print("Uso de IN")
lista = [1, 2, 3, 4, 5]
numero = int(input("Dame un numero: "))
if numero in lista:
    print("El numero esta dentro de la lista")
else:
    print("El numero no esta en la lista, pero se agregara")
    lista.append(numero)
print(lista)

# Usar NOT
print("")
print("Uso de NOT")
numero = int(input("Dame un numero: "))
if numero not in lista:
    print("El numero no esta dentro de la lista, pero se agregara")
    lista.append(numero)
else:
    print("El numero esta en la lista")
print(lista)

# Uso de AND y OR
print("")
print("Uso de and y or:")
lista_inicial = [1, 2, 3, 4, 5]
if numero in lista_inicial and nombre == "Amaya":
    print("El numero esta en la lista inicial y se llama Amaya")
elif numero in lista_inicial or nombre == "Amaya":
    print("O el numero esta en la lista inicial o el se llama Amaya")
else:
    print("No es Amaya y el numero no esta en lista")