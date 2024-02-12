# Realizar un programa que simule el juego de las tres en raya. 
# Cada jugador solo debe colocar su ficha una vez por turno y 
# no debe ser sobre una casilla ya ocupada. 
# En caso de que el jugador haga trampa el ganador será el otro. 
#Para ganar se debe conseguir realizar una línea recta (horizontal, vertical 
# o diagonal) con la misma ficha. 
# El tablero es de 3x3 y cualquier casilla podrá estar vacía u ocupada sólo 
# por una ficha X o 0. El programa debe realizar las siguientes operaciones:

# Mostrar el tablero por pantalla.
# Poner una ficha en una cuadricula comprobando que no está ocupada.
# Comprobar si se produce tres en raya e indicar si es de X o de O, o si hay empate.

def mostrar_tablero(tablero):
    for fila in tablero:
        print (fila)

def agregar_ficha(x,y,ficha,tablero):
    if tablero[y][x] == ' ':
            tablero[y][x] = ficha
            return True
    else:
            print('Esta casilla esta ocupada, elige otra')
            return False

def turno_jugador(ficha_anterior):
    while True:
            try:
                x = int(input('Dame la coordenada x (de izquierda a derecha, 1-3): ')) - 1
                y = int(input('Dame la coordenada y (de arriba hacia abajo, 1-3): ')) - 1
                ficha = input('Elige tu ficha (X o O): ').upper()
                if 0 <= x <= 2 and 0 <= y <= 2 and ficha in ['X', 'O']:
                    if ficha_anterior and ficha == ficha_anterior[-1]:
                        print('Trampa detectada. Jugador descalificado.')
                        return x, y, ficha, True
                    return x, y, ficha, False
                else:
                    print("Entrada inválida. Inténtalo de nuevo.")
            except ValueError:
                print("Por favor, introduce un número válido.")

def todos_iguales(lista):
    if lista[0] == ' ':  # Evita considerar una línea de espacios vacíos como ganadora
        return False
    return all(element == lista[0] for element in lista)

def verificar_turno(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if todos_iguales(tablero[i]) or todos_iguales([tablero[j][i] for j in range(3)]):
            return True

    # Verificar diagonal principal y secundaria
    if todos_iguales([tablero[i][i] for i in range(3)]) or todos_iguales([tablero[i][2-i] for i in range(3)]):
        return True

    return False

def juego_de_gato():
    tablero = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' '],
    ]
    ficha_anterior = []
    movimientos = 0
    while movimientos < 9:
        mostrar_tablero(tablero)
        x, y, ficha, trampa = turno_jugador(ficha_anterior)
        if trampa:
            return
        if agregar_ficha(x, y, ficha, tablero):
            ficha_anterior.append(ficha)
            movimientos += 1
            if movimientos >= 5 and verificar_turno(tablero):
                mostrar_tablero(tablero)
                print(f'Jugador con ficha {ficha} gana!')
                return
        else:
            continue
    mostrar_tablero(tablero)
    print('Empate!')

juego_de_gato()
