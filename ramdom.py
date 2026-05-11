import random

numero_secreto = random.randint(1, 100)
intento = None

while intento != numero_secreto:
    intento = int(input("Adivina el numero entre 1 y 100: "))
    
    if intento < numero_secreto:
        print("Muy bajo")
    elif intento > numero_secreto:
        print("Muy alto")
    else:
        print("¡Haz adivinado el número!")