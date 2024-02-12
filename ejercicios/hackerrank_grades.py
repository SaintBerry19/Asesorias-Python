# Iniciarlizar variables
cantidad=int(input())
lista_alumnos=[]
lista_calificaciones=[]
lista_nombres=[]

# Construir listas
for x in range(cantidad):
    nombre=input()
    calificacion=float(input())
    info_alumno= [nombre, calificacion]
    lista_alumnos.append(info_alumno)
    lista_calificaciones.append(calificacion)

# Ordenar listas
lista_calificaciones_ordenadas=list(sorted(set(lista_calificaciones)))

# Obtener segunda calificacion
segunda_calificacion = lista_calificaciones_ordenadas[1] if len(lista_calificaciones_ordenadas) > 1 else lista_calificaciones_ordenadas[0]

# Iterar para buscar los nombres que tengan la calificacion y agregarlos a la lista
for nombre,calificacion in lista_alumnos:
    if calificacion == segunda_calificacion:
        lista_nombres.append(nombre)

# Ordenar la lista e imprimir los nombres
lista_nombres=sorted(set(lista_nombres))
for nombre in lista_nombres:
    print(nombre)

# Usando Diccionarios
# Initialize variables
cantidad = int(input())
alumnos_dict = {}

# Build dictionary
for _ in range(cantidad):
    nombre = input()
    calificacion = float(input())
    if calificacion in alumnos_dict:
        alumnos_dict[calificacion].append(nombre)
    else:
        alumnos_dict[calificacion] = [nombre]

# Sort and find the second highest grade
sorted_grades = sorted(set(alumnos_dict.keys()))
segunda_calificacion = sorted_grades[1] if len(sorted_grades) > 1 else sorted_grades[0]

# Sort and print names
for nombre in sorted(alumnos_dict[segunda_calificacion]):
    print(nombre)

# Metodo de indices
    
# Subir alumnos y calificaciones
cantidad=int(input())
alumnos=[ ]
calificaciones=[]
for x in range(cantidad):
    nombre=input()
    calificacion=int(input())
    calificaciones.append(calificacion)
    alumnos.append(nombre)

# Obtener la segunda calificacion mas baja
segunda_calificacion_lista=list(set(sorted(calificaciones)))
segunda_calificacion=segunda_calificacion_lista[1] if len(segunda_calificacion_lista) > 1 else segunda_calificacion_lista[0]

# Nombres con la segunda calificacion mas baja
nombres=[]
for indice,elemento in enumerate(calificaciones):
    if elemento == segunda_calificacion:
        nombres.append(alumnos[indice])

for nombre in sorted(nombres):
    print(nombre)

