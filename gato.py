import random

RESET = "\033[0m"
AZUL = "\033[34m"
ROJO = "\033[31m"

def cambia_color(color, texto):
    return f"{color}{texto}{RESET}"

# Imprime tablero
def print_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def es_empate(tablero):
    for fila in tablero:
        if ' ' in fila:
            return False
    return True

def jugador_mueve(tablero, simbolo):
    fila, columna = -1, -1
    while fila < 0 or fila > 2 or columna < 0 or columna > 2 or tablero[fila][columna] != ' ':
        try:
            fila = int(input("Ingrese el número de fila (0, 1 o 2): "))
            columna = int(input("Ingrese el número de columna (0, 1 o 2): "))
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
            continue
    tablero[fila][columna] = simbolo

def computadora_mueve(tablero, simbolo):
    while True:
        ###################
        #Diagonal 
        if ((tablero[0][0] == "X" and tablero[1][1] == "X") or (tablero[0][0] == "O" and tablero[1][1] == "O")) and tablero[2][2] == ' ':
            tablero[2][2] = simbolo
            break

        elif ((tablero[1][1] == "X" and tablero[2][2] == "X") or (tablero[1][1] == "O" and tablero[2][2] == "O")) and tablero[0][0] == ' ':
            tablero[0][0] = simbolo 
            break

        elif ((tablero[0][0] == "X" and tablero[2][2] == "X") or (tablero[0][0] == "O" and tablero[2][2] == "O")) and tablero[1][1] == ' ':
            tablero[1][1] = simbolo 
            break

        #Diagonal 2
        elif ((tablero[0][2] == "X" and tablero[1][1] == "X") or (tablero[0][2] == "O" and tablero[1][1] == "O")) and tablero[2][0] == ' ':
            tablero[2][0] = simbolo
            break

        elif ((tablero[1][1] == "X" and tablero[2][0] == "X") or (tablero[1][1] == "O" and tablero[2][0] == "O")) and tablero[0][2] == ' ':
            tablero[0][2] = simbolo 
            break

        elif ((tablero[0][2] == "X" and tablero[2][0] == "X") or (tablero[0][2] == "O" and tablero[2][0] == "O")) and tablero[1][1] == ' ':
            tablero[1][1] = simbolo 
            break

        ###### filas
        # fila 0
        elif ((tablero[0][0] == "X" and tablero[0][1] == "X") or (tablero[0][0] == "O" and tablero[0][1] == "O")) and tablero[0][2] == ' ':
            tablero[0][2] = simbolo
            break

        elif ((tablero[0][0] == "X" and tablero[0][2] == "X") or (tablero[0][0] == "O" and tablero[0][2] == "O")) and tablero[0][1] == ' ':
            tablero[0][1] = simbolo 
            break

        elif ((tablero[0][1] == "X" and tablero[0][2] == "X") or (tablero[0][1] == "O" and tablero[0][2] == "O")) and tablero[0][0] == ' ':
            tablero[0][0] = simbolo 
            break

        # fila 1
        elif ((tablero[1][0] == "X" and tablero[1][1] == "X") or (tablero[1][0] == "O" and tablero[1][1] == "O")) and tablero[1][2] == ' ':
            tablero[1][2] = simbolo
            break

        elif ((tablero[1][0] == "X" and tablero[1][2] == "X") or (tablero[1][0] == "O" and tablero[1][2] == "O")) and tablero[1][1] == ' ':
            tablero[1][1] = simbolo 
            break

        elif ((tablero[1][1] == "X" and tablero[1][2] == "X") or (tablero[1][1] == "O" and tablero[1][2] == "O")) and tablero[1][0] == ' ':
            tablero[1][0] = simbolo 
            break

        # fila 2
        elif ((tablero[2][0] == "X" and tablero[2][1] == "X") or (tablero[2][0] == "O" and tablero[2][1] == "O")) and tablero[2][2] == ' ':
            tablero[2][2] = simbolo
            break

        elif ((tablero[2][0] == "X" and tablero[2][2] == "X") or (tablero[2][0] == "O" and tablero[2][2] == "O")) and tablero[2][1] == ' ':
            tablero[2][1] = simbolo 
            break

        elif ((tablero[2][1] == "X" and tablero[2][2] == "X") or (tablero[2][1] == "O" and tablero[2][2] == "O")) and tablero[2][0] == ' ':
            tablero[2][0] = simbolo 
            break

        ###### columnas
        # columna 0
        elif ((tablero[0][0] == "X" and tablero[1][0] == "X") or (tablero[0][0] == "O" and tablero[1][0] == "O")) and tablero[2][0] == ' ':
            tablero[2][0] = simbolo
            break

        elif ((tablero[0][0] == "X" and tablero[2][0] == "X") or (tablero[0][0] == "O" and tablero[2][0] == "O")) and tablero[1][0] == ' ':
            tablero[1][0] = simbolo 
            break

        elif ((tablero[1][0] == "X" and tablero[2][0] == "X") or (tablero[1][0] == "O" and tablero[2][0] == "O")) and tablero[0][0] == ' ':
            tablero[0][0] = simbolo 
            break

        # columna 1
        elif ((tablero[0][1] == "X" and tablero[1][1] == "X") or (tablero[0][1] == "O" and tablero[1][1] == "O")) and tablero[2][1] == ' ':
            tablero[2][1] = simbolo
            break

        elif ((tablero[0][1] == "X" and tablero[2][1] == "X") or (tablero[0][1] == "O" and tablero[2][1] == "O")) and tablero[1][1] == ' ':
            tablero[1][1] = simbolo 
            break

        elif ((tablero[1][1] == "X" and tablero[2][1] == "X") or (tablero[1][1] == "O" and tablero[2][1] == "O")) and tablero[0][1] == ' ':
            tablero[0][1] = simbolo 
            break

        # columna 2
        elif ((tablero[0][2] == "X" and tablero[1][2] == "X") or (tablero[0][2] == "O" and tablero[1][2] == "O")) and tablero[2][2] == ' ':
            tablero[2][2] = simbolo
            break

        elif ((tablero[0][2] == "X" and tablero[2][2] == "X") or (tablero[0][2] == "O" and tablero[2][2] == "O")) and tablero[1][2] == ' ':
            tablero[1][2] = simbolo 
            break

        elif ((tablero[1][2] == "X" and tablero[2][2] == "X") or (tablero[1][2] == "O" and tablero[2][2] == "O")) and tablero[0][2] == ' ':
            tablero[0][2] = simbolo 
            break

        ###################

        else:
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)
            if tablero[fila][columna] == ' ':
                tablero[fila][columna] = simbolo
                break

def verifica_ganador(tablero, simbolo):
    for fila in tablero:
        if all(s == simbolo for s in fila):
            return True
    for columna in range(3):
        if all(tablero[fila][columna] == simbolo for fila in range(3)):
            return True
    if all(tablero[i][i] == simbolo for i in range(3)) or all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

def juego_gato():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    print("¡Bienvenido al juego de Gato!")
    
    jugador_simbolo = input("Seleccione su símbolo ('X' o 'O'): ").upper()
    if jugador_simbolo != 'X' and jugador_simbolo != 'O':
        print("Símbolo no válido. Se seleccionará 'X' por defecto.")
        jugador_simbolo = 'X'

    if jugador_simbolo == 'X':
        computadora_simbolo = 'O'
    else:
        computadora_simbolo = 'X'
    
    turno = 'X'
    while True:
        print_tablero(tablero)
        
        if turno == jugador_simbolo:
            print(cambia_color(AZUL, "Es su turno."))
            jugador_mueve(tablero, jugador_simbolo)
        else:
            print(cambia_color(ROJO, "Turno de la computadora."))
            computadora_mueve(tablero, computadora_simbolo)
        
        if verifica_ganador(tablero, turno):
            print_tablero(tablero)
            print(f"¡{turno} ha ganado! ¡Felicidades!")
            break
        elif es_empate(tablero):
            print_tablero(tablero)
            print("¡Es un empate!")
            break
        
        turno = 'X' if turno == 'O' else 'O'

if __name__ == "__main__":
    juego_gato()
