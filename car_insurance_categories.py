# The Car Insurance
# A car insurance company has 4 types of packages, ordered from the least to the most
# expensive : Green, Blue, Orange & Red.
# If the driver is less than 25 years old and his driving license was acquired up to 2 years ago,
# the company will propose the Red offer. However, if the driver had an accident, the company
# will refuse to insure him.
# If the driver is less than 25 years old but his driving license was acquired more than 2 years
# ago, the company will propose the Orange offer. Similarly, if the driver had an accident, the
# company will refuse to insure him.
# The company will do the same for drivers that are more than 25 years old with a driving
# license acquired less than two years ago.
# If the driver is more than 25 years old and his driving license was acquired more than 2
# years ago, the company will propose the Blue offer. If the driver had an accident, the
# company will propose the Orange offer. If the driver had two accidents, the company will
# propose the Red offer.
# Finally, the company will reward their customers that bought insurance for 5 years
# consecutively by reducing the cost of their insurance by one level. ex : a Blue package
# becomes a Green one.
# Ask a user for his age, his driving license age, his seniority in the insurance and his
# number of accidents.
# Give the proper insurance offer to the user.
edad = int(input("¿Cual es tu edad?"))
licencia = int(input("¿Cuanto tienes con tu licencia"))
accidentes = int(input("¿Cuantos accidentes has sufrido?"))
antiguedad = int(input("¿Cuanto tienes en la empresa?"))

paquete = ""

if edad < 25 and licencia < 2 and accidentes < 1:
    paquete = "rojo"

elif edad < 25 and licencia > 2 and accidentes < 1:
    paquete = "naranja"

elif edad > 25 and licencia > 2:

    if accidentes == 0:
        paquete = "azul"

    elif accidentes == 1:
        paquete = "naranja"

    elif 1 < accidentes:
        paquete = "rojo"
else:
    print("No hay paquete para ti!")
    exit()

if antiguedad > 5:
    if paquete == "rojo":
        paquete == "naranja"
    elif paquete == "naranja":
        paquete == "azul"
    elif paquete == "azul":
        paquete = "verde"

print(f"Perteneces a la categoria {paquete}")
