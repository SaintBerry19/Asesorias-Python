# Tabla de Veradad

# AND
print(True and False)
print(True and True)
print(False and False)

# OR
print(True or False)
print(True or True)
print(False or False)

# Condiocionales
# IF, ELIF, ELSE , se utilizan para hacer una comparacion y generar una condicion de cumplimiento.
# Tiene la estrucutra IF condicion:  (SI ESTO)
#                           entonces ejecuta esto
#                     ELIF condicion: (SI ESTO OTRO)
#                           entonces ejecuta esto
#                     ELSE: (SI NINGUNA DE LAS ANTERIORES)
#                           entonces ejecuta esto
# solo se ejecutara 1 de los tres, si entras en el if aunque el elif tambien sea verdad no lo ejecutara
# Los operados condicionales/logicos son los siguientes, ==,<=,>=,!=,NOT, AND, OR, IN.
numero = 1

if numero < 10 and numero % 3 == 0:
    print(numero,"if")
elif numero > 10 and numero % 3 != 0 :
    print(numero,"elif")
elif numero > 10  and numero % 3 == 0:
    print(numero,"elif2")
else:
    print("Hola soy German")


if numero < 10:
    if numero % 3 == 0:
        print(f"El numero {numero} es menor que 10 y es divisile entre 3") 
    else:
        print(f"El numero {numero} es menor que 10 y no es divisile entre 3") 
else:
    if numero % 3 == 0:
        print(f"El numero {numero} es menor que 10 y es divisile entre 3") 
    else:
        print(f"El numero {numero} es menor que 10 y no es divisile entre 3")


if not (numero!=10):
    print("Numero ES 10")
elif numero > 10:
    print("Numero es mayor que 10")
else:
    print("El numero es menor 10")
    
# print("")
# print("Uso de condicionales")
# nombre = input("Dime tu nombre: ")
# oracion = f"Hola me llamo {nombre}"

# if oracion == "Hola me llamo Amaya":
#     print("Se llama Amaya")
# elif oracion == "Hola me llamo Roberto":
#     print("Se llama Roberto")
# else:
#     print("No es ni Amaya ni Roberto")

