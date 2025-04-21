oracion = "Hola me llamo Roberto"
nombre = "Roberto Mora"
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