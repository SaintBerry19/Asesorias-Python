# El ejercicio tradicional para determinar si un año es bisiesto 
# o no se basa en las siguientes reglas:

# Si un año es divisible por 4, es un candidato a ser bisiesto.
# Si un año es divisible por 100, no es bisiesto, a menos que:
# Si un año es divisible por 400, entonces sí es bisiesto.

entry=int(input("Dame un año para verificar si es bisiesto: "))
if( entry % 4 == 0 and entry % 100 != 0) or entry % 400 == 0:
    print ("El año es bisiesto")
else:
    print ("El año no es bisiesto")