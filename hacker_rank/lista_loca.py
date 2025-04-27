# # Ask for input
# numbers = input("Enter 10 numbers separated by space: ")

# # Create the list by splitting the input
# number_list = numbers.split(",")

# # Optionally, convert the list to integers
# number_list = [int(num) for num in number_list]

# print(number_list)


# Ejemplo 1
# Ask for input
numbers = input("Enter 10 numbers separated by space: ")

# Create the list by splitting and mapping to int
number_list = list(map(int, numbers.split(",")))

for anio in number_list:
    if( anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print ("El año es bisiesto")
    else:
        print ("El año no es bisiesto")


# Ejemplo 2
while True:
    anio = int(input())
    if( anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print ("El año es bisiesto")
    else:
        print ("El año no es bisiesto")
        break

# Ejemplo 3
# Ask for input
numbers = input("Enter 10 numbers separated by space: ")

# Create the list by splitting and mapping to int
number_list = list(map(int, numbers.split(",")))

for anio in number_list:
    if( anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print ("El año es bisiesto")
    else:
        print ("El año no es bisiesto")
        break