import random

def generar_numero_ponderado(x, z, porcentajes):
    # Crear una lista vacía para almacenar los números con base en sus porcentajes
    lista_ponderada = []
    
    # Llenar la lista_ponderada basado en los porcentajes
    for numero in range(x, z + 1):
        # Añadir cada número a la lista basado en su porcentaje
        veces = int(porcentajes[numero] * 100)  # Asumiendo que los porcentajes son decimales
        lista_ponderada.extend([numero] * veces)
    
    # Elegir un número aleatoriamente de la lista ponderada
    numero_elegido = random.choice(lista_ponderada)
    
    return numero_elegido

# Definir los porcentajes para cada número entre x y z
porcentajes = {
    1: 0.1,  # 10%
    2: 0.2,  # 20%
    3: 0.3,  # 30%
    4: 0.4   # 40%
}

# Generar el número aleatorio ponderado
numero_aleatorio = generar_numero_ponderado(1, 4, porcentajes)
print(f"El número aleatorio ponderado es: {numero_aleatorio}")
