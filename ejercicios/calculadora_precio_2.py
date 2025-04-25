peso = float(input("dame el peso del paquete en KG: "))
distancia = float(input("dame la distancia del envio en KM: "))
costo_total = 0
descuento = 0

if peso <= 2:
    costo_base = 5
    precio_km = .10
elif peso > 2 and peso <= 5:
    costo_base = 10
    precio_km = .15
elif peso > 5 and peso <= 10:
    costo_base = 15
    precio_km = .2
else:
    costo_base = 20
    precio_km = .25

costo_total = costo_base + distancia*precio_km

if distancia > 500 and distancia <= 1000:
    descuento = .05 
elif distancia > 1000:
    descuento = .10 

print(f"su costo total es:${costo_total * (1 - descuento)}")