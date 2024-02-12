def mostrar_tablero(tablero):
    for row in tablero:
        print(row)

def turno_jugador():
    x = int(input("X: ")) - 1
    y = int(input("Y: ")) - 1
    ficha = input("X o 0: ")
    return x, y, ficha

def agregar_ficha(x, y, ficha, turno, tablero):
    if turno and ficha == turno[-1]:
        print("Trampa detectada. Jugador descalificado.")
        return False
    else:
        if tablero[y][x] == "":
            tablero[y][x] = ficha
            turno.append(ficha)
        else:
            print("Esta ocupado elige otro lugar")
    return True

def verificar_igualdad(lista):
    if lista[0] == ' ':  # Evita considerar una línea de espacios vacíos como ganadora
        return False
    return all(element == lista[0] for element in lista)
        
def verificar_victoria(tablero):
    # Ganar por filas o columnas
    for i in range(3):
        if verificar_igualdad(tablero[i]) or verificar_igualdad([tablero[i][j] for j in range(3)]):
            return True

    # Ganar por diagonal o diagonal secundaria
    if verificar_igualdad([tablero[i][i] for i in range(3)]) or verificar_igualdad([tablero[i][2-i] for i in range(3)]):
        return True
       
    return False


def juego_gato():
    tablero = [["", "", ""], ["", "", ""], ["", "", ""]]
    turno = []
    turnos = 1
    while turnos < 10:
        mostrar_tablero(tablero)
        x, y, ficha = turno_jugador()
        validez = agregar_ficha(x, y, ficha, turno, tablero)
        if not validez:
            return
        if verificar_victoria(tablero):
            mostrar_tablero(tablero)
            print(f'Jugador con las fichas {ficha} ha ganado!')
            return
        turnos += 1
    mostrar_tablero(tablero)
    print("Esto es un empate!")


juego_gato()
