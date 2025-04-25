def calculadora_precio(peso, distancia):
    costo_total = None
    descuento = 0
    if peso <= 2:
        costo_base = 5
        precio_km = 0.10
    elif peso > 2 and peso <= 5:
        costo_base = 10
        precio_km = 0.15
    elif peso > 5 and peso <= 10:
        costo_base = 15
        precio_km = 0.2
    else:
        costo_base = 20
        precio_km = 0.25

    costo_total = costo_base + distancia * precio_km

    if distancia > 500 and distancia <= 1000:
        descuento = 0.05
    elif distancia > 1000:
        descuento = 0.10

    return costo_total * (1 - descuento)


valor_1 = calculadora_precio(259, 112323)
valor_2 = calculadora_precio(249, 112312323)
valor_3 = calculadora_precio(2339, 112323)
valor_4 = calculadora_precio(219, 312323)
print(valor_1, valor_2, valor_3, valor_4)
