# Las reglas para calcular el costo son las siguientes:


# Para paquetes que pesen hasta 2 kg, el costo base es de $5.00. Cada kilómetro añade $0.10 al costo.
# Para paquetes que pesen más de 2 kg pero menos de o igual a 5 kg, el costo base es de $10.00. Cada kilómetro añade $0.15 al costo.
# Para paquetes que pesen más de 5 kg pero menos de o igual a 10 kg, el costo base es de $15.00. Cada kilómetro añade $0.20 al costo.
# Para paquetes que pesen más de 10 kg, el costo base es de $20.00. Cada kilómetro añade $0.25 al costo.
# Para distancias de más de 500 km pero menos de o igual a 1000 km, se aplica un descuento del 5% sobre el costo total del envío.
# Para distancias mayores a 1000 km, se aplica un descuento del 10% sobre el costo total del envío.
# Tu tarea es escribir un programa que solicite al usuario el peso del paquete (en kg) y la distancia del envío (en km), y luego calcule y muestre el costo total del envío.


def calculadora_de_precio(peso, distancia):
    # Determinar el costo base y el costo por kilómetro según el peso
    if peso <= 2:
        costo_base = 5.00
        costo_por_km = 0.10
    elif 2 < peso <= 5:
        costo_base = 10.00
        costo_por_km = 0.15
    elif 5 < peso <= 10:
        costo_base = 15.00
        costo_por_km = 0.20
    else:  # peso > 10
        costo_base = 20.00
        costo_por_km = 0.25

    # Calcular el costo total antes del descuento
    costo_total = costo_base + (costo_por_km * distancia)

    # Aplicar descuentos por distancia
    if 500 < distancia <= 1000:
        descuento = costo_total * 0.05
        costo_total -= descuento
    elif distancia > 1000:
        descuento = costo_total * 0.10
        costo_total -= descuento
    return costo_total, descuento


peso = float(input("Dame el peso del paquete(kg): "))
distancia = float(input("Dame la distancia del envio(km): "))
costo_total = calculadora_de_precio(peso, distancia)
print(f"El costo total del envio es de ${costo_total}")
