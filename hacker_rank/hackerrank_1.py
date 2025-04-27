record_estudiantes = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    record_estudiantes.append([name,score])

diccionario_alumnos_calificaciones  = {}
calificaciones = []

diccionario_alumnos_calificaciones = {}

for estudiante, score in record_estudiantes:
    if score not in diccionario_alumnos_calificaciones:
        diccionario_alumnos_calificaciones[score] = []
    diccionario_alumnos_calificaciones[score].append(estudiante)

# Ordenar las calificaciones
calificaciones_ordenadas = sorted(diccionario_alumnos_calificaciones.keys())

segunda_calificacion_mas_baja = calificaciones_ordenadas[1]

alumnos_con_segunda_baja = sorted(diccionario_alumnos_calificaciones[segunda_calificacion_mas_baja])

# Imprimir los nombres
for alumno in alumnos_con_segunda_baja:
    print(alumno)

record_estudiantes = []

# # Input de los datos
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     record_estudiantes.append([name, score])

# # Extraer todas las calificaciones
# calificaciones = sorted({score for _, score in record_estudiantes})

# # Segunda calificación más baja
# segunda_mas_baja = calificaciones[1]

# # Filtrar los alumnos con esa calificación
# alumnos_segunda_baja = sorted([name for name, score in record_estudiantes if score == segunda_mas_baja])

# # Imprimir los nombres
# for alumno in alumnos_segunda_baja:
#     print(alumno)
