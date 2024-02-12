import time
import matplotlib.pyplot as plt

def menor_numero_divisible(n):
    # Empezaremos asignando el numero menor como el numero ingresado por el usuario como primera iteracion, y mediremos el tiempo
    # de ejecucion.
    numero_menor = n
    iteracion = 1
    start_time = time.time()

    # Empezamos la iteracion.
    while True:

        # Bandera para la respuesta.
        divisible = True
        
        # Checar si los numeros de 2 a n son divisibles por el numero menor, si no la bandera cambia a falso.
        for i in range(2, n + 1):
            if numero_menor % i != 0:
                divisible = False
                break
        
        # Si el for de arriba no cambio la bandera, entramos a esta condicion y tenemos la respuesta, terminamos de medir
        # el tiempo.
        if divisible:
            end_time = time.time()
            return numero_menor, iteracion,end_time - start_time
                
        # Si no entramos a la condicion pasada aun no tenemos la respuesta y sumamos 1 al numero y a la iteracion.
        numero_menor += 1
        iteracion += 1

def menor_numero_divisible_euclides(n):
    start_time = time.time()
    def mcm(a, b):
        producto = a * b
        while b:
            a, b = b, a % b
        mcd = producto // a
        return mcd

    resultado_mcm = 2
    for i in range(3, n + 1):
        resultado_mcm = mcm(resultado_mcm, i)
    end_time = time.time()
    return resultado_mcm, end_time - start_time

n = int(input("Give me a number: "))
numero,iteracion,tiempo = menor_numero_divisible(n)
print(f'''El menor numero que puede ser dividido por los numeros entre 2 y {n} es: {numero}
Se encontro el numero en la iteracion: {iteracion}
Tardo {tiempo}''')
resultado_final_mcm,tiempo_euclides = menor_numero_divisible_euclides(n)
print(f'''El menor numero que puede ser dividido por los numeros entre 2 y {n} es: {numero}
Tardo {tiempo_euclides}''')

# Prueba con diferentes valores de n
n_values = range(2, 20)  # Puedes cambiar el rango según sea necesario
tiempo_acumulado_metodo1 = []
tiempo_acumulado_metodo2 = []
tiempo_anterior1 = 0
tiempo_anterior2 = 0

for n in n_values:
    _, _, tiempo1 = menor_numero_divisible(n)
    _, tiempo2 = menor_numero_divisible_euclides(n)
    tiempo_anterior1 += tiempo1
    tiempo_anterior2 += tiempo2
    tiempo_acumulado_metodo1.append(tiempo_anterior1)
    tiempo_acumulado_metodo2.append(tiempo_anterior2)

# Graficar los resultados
plt.plot(n_values, tiempo_acumulado_metodo1, label='Metodo Fuerza Bruta')
plt.plot(n_values, tiempo_acumulado_metodo2, label='Metodo Euclides')
plt.xlabel('n')
plt.ylabel('Tiempo Acumulado (s)')
plt.title('Comparación de Tiempos de Ejecución Acumulados')
plt.legend()
plt.show()