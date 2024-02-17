# Primera Clase - Tipos de Datos
# - String (Caracteres)
# - Integer (int)
# - Float (float)

# El signo de igual toma la funcion de referenciar y asignar algo a una variable. Pero tomara en cuenta si ese algo es mutable o inmutable.
# Mutabilidad = El valor de dicho objeto/elemento puede ser alterado (listas, variables, diccionarios)
# Inmutabilidad = El valor no puede ser alterado (strings, integers, floats)
# Nota: la funcion print sirve para mostrar en la consola, para cadenas de caracteres necesitas las comillas, para variables, funciones, numeros, no necesitas comillas.

# a = 1
# b = a
# b = 1 + 1
# print(b)
# print(a)

# a = [1,2,3]
# b = a
# b.append(4)
# print(b)
# print(a)

# Strings (Cadena de caracteres)
# Print puede utilizar varios inputs, o variables, solo debes separar con las comas.
cadena_caracteres = "Hola mundo, me llamo Amaya"
cadena_2 = "y soy lo maximo!"
print(cadena_caracteres, "!", cadena_2, 3 + 1, "Hola", [1, 2, 3, 4, 5])
sujeto = "Nuestro amigo Juan,"
predicado = " va a cocinar un huevito estrellado."
oracion = sujeto + predicado
print(oracion)

# Es importante saber que los strings son iterables, es decir, estan compuestos de elementos sencillos a los cuales, se puede acceder usando la indexacion.
# Index, es el valor de referencia de un elemento, dentro de un iterable, siempre empieza en 0.
# Si tenemos el string "Hola mundo!", podemos decir que esta compuesto de la suma de todos sus elementos(caracteres), en este caso serian 11 elementos.
# Al tener 11 elementos el primer elemento se representa con el valor 0, entonces el ultimo, en este caso se representa con el numero 10.
# Para utilizar el metodo de indexacion basta con escribir el nombre de la variable seguido de los simbolos [], y dentro ira el indice al cual se desea acceder.
print(oracion[2])
# Tambien se pueden utilizar rangos de indexacion, para esto se utiliza la siguiente estrucutra[inicio:fin:paso], es importante
# saber que el inicio es incluyente y el final es excluyente y el paso es opcional siendo 1 el default, es decir si tenemos lo siguiente [1:5]
# la indexacion ira de 1 en 1 desde el 1 al 5 sin contar el 5.
# La indexacion por rango recibe el nombre de Slicing.
print(oracion[0:7])
# Puedes usar la notacion [:] para que te imprima todo, es decir no asignar un valor en especifico toma por default el inicio y el fin, esto sirve si quieres
# imprimir toda la expresion usando un tipo de salto distinto.
print(oracion[::3])
# Puedes usar notaciones negativas y saltos negativos para voltear strings. Nota: para la indexacion negativa el ultimo elemento SI ES -1 no -0.
print(oracion[-4:])
nombre = "aroM otreboR"
print(nombre[::-1])
# Los string tienen varios metodos incluidos en su clase, una clase es una agrupcion de objetos con las mismas caracteristicas.
# Los metodos son funciones pertenecientes a una clase, siendo que una funcion es una agrupacion de codigo.
# El metodo index siempre te dira la primera ocurrencia.
print(oracion.index("v"))

# NOTA IMPORTANTE Pequenia explicacion de la diferencia de una funcion y un metodo,
# Esto es una funcion y se accede de la siguiente manera:
# def index_2(oracion):
#     for i in range(0, len(oracion)):
#         if oracion[i] == "v":
#             return i
#     return -1 # Retorna -1 si no se encuentra la letra "v"

# indice = index_2(oracion)
# print(indice)

# # Esto es una clase y se accede de la siguiente manera:
# class Palabra:
#     def __init__(self, oracion):
#         self.oracion = oracion

#     def index_2(self):
#         for i in range(0, len(self.oracion)):
#             if self.oracion[i] == "v":
#                 return i
#         return -1  # Retorna -1 si no se encuentra la letra "v"

# mi_palabra = Palabra(oracion)
# indice_v = mi_palabra.index_2()
# print(f"El índice de la primera 'v' es: {indice_v}")

# Trucos del print
print(
    f"Esta manera de imprimir nos permite meter variables dentro de una cadena de caracteres {oracion} Me llamo {nombre[::-1]}"
)
print(
    "Esta manera de imprimir nos permite meter variables dentro de una cadena de caracteres",
    oracion,
    "Me llamo",
    nombre[::-1],
)
print(
    f"""Esta manera de imprimir nos permite 
meter variables dentro de una 
cadena de caracteres {oracion} 
Me llamo {nombre[::-1]}
"""
)
