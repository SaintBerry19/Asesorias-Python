# # The Car Insurance
# # A car insurance company has 4 types of packages, ordered from the least to the most
# # expensive : Green, Blue, Orange & Red.

# # Ask a user for his age, his driving license age, his seniority in the insurance and his
# # number of accidents.
# # Give the proper insurance offer to the user.

# edad = int(input("¿Cual es tu edad?"))
# licencia = int(input("¿Cuanto tienes con tu licencia"))
# accidentes = int(input("¿Cuantos accidentes has sufrido?"))
# antiguedad = int(input("¿Cuanto tienes en la empresa?"))
# valor = None
# seguros = ['Green', 'Blue', 'Orange', 'Red']
# # If the driver is less than 25 years old and his driving license was acquired up to 2 years ago,
# # the company will propose the Red offer. However, if the driver had an accident, the company
# # will refuse to insure him.

# if edad <= 25 and licencia <= 2 and accidentes == 0:
#     valor = 3

# # If the driver is less than 25 years old but his driving license was acquired more than 2 years ago, the company will propose the Orange offer. 
# # Similarly, if the driver had an accident, the company will refuse to insure him.

# elif edad <= 25 and licencia > 2 and accidentes == 0:
#     valor = 2

# # The company will do the same for drivers that are more than 25 years old with a driving license acquired less than two years ago.
# elif edad > 25 and licencia <= 2 and accidentes == 0:
#     valor = 2

# # If the driver is more than 25 years old and his driving license was acquired more than 2 years ago, the company will propose the Blue offer.
# elif edad > 25 and licencia > 2 and accidentes == 0:
#     valor = 1

# # If the driver had an accident, the company will propose the Orange offer.
# elif edad > 25 and licencia > 2 and accidentes == 1:
#     valor = 2

# # If the driver had two accidents, the company will propose the Red offer.
# elif edad > 25 and licencia > 2 and accidentes == 2:
#     valor = 3

# else:
#     print("Chingas a tu madre")

# # Finally, the company will reward their customers that bought insurance for 5 years
# # consecutively by reducing the cost of their insurance by one level. ex : a Blue package
# # becomes a Green one.
# if antiguedad > 5:
#     valor = valor - 1

# print(f'Eres {seguros[valor]}')

# Metodo Fresa
# Evaluación base de riesgo
edad = int(input("¿Cuál es tu edad? "))
licencia = int(input("¿Cuánto tiempo tienes con tu licencia? "))
accidentes = int(input("¿Cuántos accidentes has tenido? "))
antiguedad = int(input("¿Cuánto tiempo tienes con la aseguradora? "))

seguros = ['Green', 'Blue', 'Orange', 'Red']
valor = None

# Casos no asegurables
if accidentes > 2 or (edad <= 25 and licencia <= 2 and accidentes > 0):
    print("Lo sentimos, no podemos asegurarte.")
else:
    if edad <= 25:
        valor = 2 if licencia > 2 else 3
    else:  # edad > 25
        valor = 1 if licencia > 2 else 2

        # Ajustes por accidentes si cumple edad y licencia
        if edad > 25 and licencia > 2 and accidentes > 0:
            valor = 2 if accidentes == 1 else 3

    # Descuento por antigüedad
    if antiguedad > 5:
        valor = max(0, valor - 1)

    print(f"Tu seguro es: {seguros[valor]}")

