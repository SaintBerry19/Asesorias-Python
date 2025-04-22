# El ejercicio tradicional para determinar si un año es bisiesto 
# o no se basa en las siguientes reglas:

# Si un año es divisible por 4 y no por 100 es bisiesto, 
# Si un año es divisible por 4 y por 100 y por 400, entonces sí es bisiesto.
anio=int(input("Dame un año para verificar si es bisiesto: "))
print("")
print("Metodo 1")
if( anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print ("El año es bisiesto")
else:
    print ("El año no es bisiesto")

# Si un año es divisible por 4, es un candidato a ser bisiesto.
# Si un año es divisible por 100, no es bisiesto, a menos que:
# Si un año es divisible por 400, entonces sí es bisiesto.
print("")
print("Metodo 2")
if anio % 400 == 0: 
    print("el anio si es bisiesto")
elif anio % 100 == 0: # anio no es divisible entre 400 porque no entraste al primer if
        print("el anio no es bisiesto")
elif anio % 4 == 0: # anio no es divisible entre 400 porque no entraste al primer if
                    # ni entre 100 porque no entraste en el elif
        print("el anio es bisiesto")
else: print("no es bisiesto")

# Si un año es divisible por 4, es un candidato a ser bisiesto.
# Si un año es divisible por 100, no es bisiesto, a menos que:
# Si un año es divisible por 400, entonces sí es bisiesto.
print("")
print("Metodo 3")
# Lineal/directa
if anio % 4 == 0: # Eres divisible entre 4?
    # Soy divisible entre 4
    if anio % 100 == 0: # Si pero soy divisible entre 100
        if anio % 400 == 0: # Si pero soy divisible entre 400
            print("Eres bisiesto")
        else: # Si pero no soy divisible entre 400
            print("No eres bisiesto")
    else: # Si pero no soy divisible entre 100
         print ("Eres bisiesto")
else: # No soy divisible entre 4
    print("No eres bisiesto")

# Si un año es divisible por 4, es un candidato a ser bisiesto.
# Si un año es divisible por 100, no es bisiesto, a menos que:
# Si un año es divisible por 400, entonces sí es bisiesto.
print("")
print("Metodo 4")
if anio % 4 == 0 and anio % 100 == 0 and anio % 400 ==0:
    print("Bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 !=0 :
    print("No Bisiesto")
elif anio % 4 == 0 and anio % 100 != 0:
    print("Bisiesto")
else:
    print("No Bisiesto")