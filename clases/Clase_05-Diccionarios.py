import json

# Diccionario es una etructura de datos donde se relacion una llave con un valor siguiendo la siguiente estructura:
# {"llave": valor}
# El valor puede tomar cualquier "valor" es decir puede ser una lista, otro diccionario, una cadena de texto, un numero.
# Son iterables y para acceder se usa la estructura diccionario["llave"]
# Son mutables

hola = {"llave": 39}
variable = [10, 11, 12, 13, 14, 15]

diccionario = {
    "numero": 1,
    "diccionario": hola["llave"],
    "lista": [0, 1, 2, 3, 4, 5],
    "variable": variable,
}
lista = diccionario["lista"]

for elemento in lista:
    print(elemento)

for elemento in variable:
    print(elemento)

print(diccionario.keys(), diccionario.values())

for llave, valor in diccionario.items():
    print(llave, ": ", valor)

diccionario["numero"] = 59

print(diccionario)

# 1. Abrir y cargar el JSON en un dict de Python
with open("clases\jsons\input.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

print(datos)

# Tu estructura de datos en Python (puede ser dict, list, etc.)
datos = {
    "nombre": "Roberto",
    "edad": 29,
    "ciudades_visitadas": ["Monterrey", "Guadalajara", "CDMX"],
    "activo": True,
}

# 1) Escribir a un archivo JSON
with open("clases\jsons\output.json", "w", encoding="utf-8") as f:
    json.dump(
        datos,  # el objeto Python a serializar
        f,  # el archivo abierto en modo escritura
        ensure_ascii=False,  # para mantener caracteres UTF-8 legibles
        indent=4,  # para formatear con sangrías (legible)
    )

print(diccionario["lista"].index(3))

alumnos = {
    "juan": {
        "espaniol": "1,2,3,4,5",
    }
}

# FORMAS DE CAMBIAR DE CADENA DE TEXTO A ARRAY NUMERICO
calificacion_espaniol = list(map(int, alumnos["juan"]["espaniol"].split(",")))
# calificacion_espaniol = [int(calificacion) for calificacion in alumnos["juan"]["espaniol"].split(",")]


# LIST COMPREHENSION
# calificacion_espaniol = [int(calificacion) for calificacion in alumnos["juan"]["espaniol"].split(",")]

# calificacion_espaniol = []
# for elemento in alumnos["juan"]["espaniol"].split(","):
#     calificacion_espaniol.append(int(elemento))

# MAP
# def sumar(x):
#     return int(x) + 10  # o lo que necesites hacer con x

# calificacion_espaniol = list(map(sumar,alumnos["juan"]["espaniol"].split(",")))

print(calificacion_espaniol)

ejemplo_enfermo = {
    "value1": [
        1,
        2,
        3,
        4,
        5,
        {
            "value1": [1, 2, 3, 4, 5],
            "value2": {"value2": [1, 2, 3, 49, 5], "value1": [1, 2, 3, 4, 5]},
            "value3": "",
        },
        6,
        7,
        8,
        9,
        10,
    ],
    "value2": 2,
    "value3": [1, 2, 3, 4, 5],
}

lista_usuarios = [
    {
        "value1": [
            1,
            2,
            3,
            4,
            5,
            {
                "value1": [1, 2, 3, 4, 5],
                "value2": {"value2": [1, 2, 3, 49, 5], "value1": [1, 2, 3, 4, 5]},
                "value3": "",
            },
            6,
            7,
            8,
            9,
            10,
        ],
        "value2": 2,
        "value3": [1, 2, 3, 4, 5],
    },
    {
        "value1": [
            1,
            2,
            3,
            4,
            5,
            {
                "value1": [1, 2, 3, 4, 5],
                "value2": {"value2": [1, 2, 3, 9, 5], "value1": [1, 2, 3, 4, 5]},
                "value3": "",
            },
            6,
            7,
            8,
            9,
            10,
        ],
        "value2": 2,
        "value3": [1, 2, 3, 4, 5],
    },
    {
        "value1": [
            1,
            2,
            3,
            4,
            5,
            {
                "value1": [1, 2, 3, 4, 5],
                "value2": {"value2": [1, 2, 3, 29, 5], "value1": [1, 2, 3, 4, 5]},
                "value3": "",
            },
            6,
            7,
            8,
            9,
            10,
        ],
        "value2": 2,
        "value3": [1, 2, 3, 4, 5],
    },
    {
        "value1": [
            1,
            2,
            3,
            4,
            5,
            {
                "value1": [1, 2, 3, 4, 5],
                "value2": {"value2": [1, 2, 3, 4, 5], "value1": [1, 2, 3, 4, 5]},
                "value3": "",
            },
            6,
            7,
            8,
            9,
            10,
        ],
        "value2": 2,
        "value3": [1, 2, 3, 4, 5],
    },
    {
        "value1": [
            1,
            2,
            3,
            4,
            5,
            {
                "value1": [1, 2, 3, 4, 5],
                "value2": {"value2": [1, 2, 3, 99, 5], "value1": [1, 2, 3, 4, 5]},
                "value3": "",
            },
            6,
            7,
            8,
            9,
            10,
        ],
        "value2": 2,
        "value3": [1, 2, 3, 4, 5],
    },
]

for usuario in lista_usuarios:
    edad_usuario = usuario["value1"][5]["value2"]["value2"][3]
    if edad_usuario >= 18:
        print(f"Puedes pasar! Eres {edad_usuario - 18} mayor que la edad minima.")
    else:
        print(f"No puedes pasar! Eres {18 - edad_usuario} menor que la edad minima.")
