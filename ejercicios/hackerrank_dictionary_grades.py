# 2 < n < 10 donde n es la cantidad de alumnos 
# 0 =< marks[i] =< 100 donde marks[i] es la calificacion
# array de calificaciones longitud de 3, es decir cada alumno puede tener 3 calificaciones

# Definir cantidad de registros e inicializar el diccionario de calificaciones
n = int(input())
calificaciones_estudiantes = {}

# Hacer el loop para el ingreso de datos
# Recordar que se pueden asignar multiples valores a distintas variables en solo 1 linea de codigo
# Siempre debe de ser 1 a 1, es decir, por cada valor debe haber una variable
# En caso de no querer se puede asignar el * a la variable para decir que lo que no este asignado a 1 variable se asigne a una lista.
# Map es una funcion que aplica otra funcion en todos los elementos de un iterable.

for _ in range(n):
    nombre,*calificaciones_string = input().split()
    calificaciones = list(map(float,calificaciones_string))
    calificaciones_estudiantes[nombre] = calificaciones
alumno = input()
promedio_redondeado = round(sum(calificaciones_estudiantes[alumno])/len(calificaciones_estudiantes[alumno]),2)
print(f"{promedio_redondeado:.2f}")
