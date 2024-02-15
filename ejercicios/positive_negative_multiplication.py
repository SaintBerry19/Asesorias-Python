# Pedir 2 numeros
numero_1 = float(input("Dame un numero: "))
numero_2 = float(input("Dame otro numero: "))

# Caso positivo o negativo
if (numero_1 > 0 and numero_2 > 0) or (numero_1 < 0 and numero_2 < 0):
    print("El resultado es positivo")
elif (numero_1 > 0 and numero_2 < 0) or (numero_1 < 0 and numero_2 > 0):
    print("El resultado es negativo")
else:  # Caso 0
    print("El resultado es 0")
