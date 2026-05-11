import random

def juego_adivinanza_dos_jugadores():
    # Generamos un número aleatorio entre 0 y 10000
    numero_secreto = random.randint(0, 10000)
    jugador_1_intentos = 0
    jugador_2_intentos = 0
    turno_jugador_1 = True  # El jugador 1 comienza

    print("¡Juego de Adivinanza para dos jugadores!")
    print("El primer jugador que adivine el número entre 1 y 100, gana.")

    while True:
        if turno_jugador_1:
            # Turno del jugador 1
            print("Turno del Jugador 1")
            adivinanza_1 = int(input("Jugador 1, ingresa tu número: "))
            jugador_1_intentos += 1

            if adivinanza_1 < numero_secreto:
                print("Muy bajo, intenta de nuevo.")
            elif adivinanza_1 > numero_secreto:
                print("Muy alto, intenta de nuevo.")
            else:
                print(f"¡Felicidades Jugador 1! Adivinaste el número en {jugador_1_intentos} intentos.")
                print(f"Jugador 2 realizó {jugador_2_intentos} intentos.")
                break
        else:
            # Turno del jugador 2
            print("Turno del Jugador 2")
            adivinanza_2 = int(input("Jugador 2, ingresa tu número: "))
            jugador_2_intentos += 1

            if adivinanza_2 < numero_secreto:
                print("Muy bajo, intenta de nuevo.")
            elif adivinanza_2 > numero_secreto:
                print("Muy alto, intenta de nuevo.")
            else:
                print(f"¡Felicidades Jugador 2! Adivinaste el número en {jugador_2_intentos} intentos.")
                print(f"Jugador 1 realizó {jugador_1_intentos} intentos.")
                break
        
        # Cambiamos el turno al otro jugador
        turno_jugador_1 = not turno_jugador_1

juego_adivinanza_dos_jugadores()