import random

def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    return fib_sequence

n = int(input("Introduce la cantidad de números Fibonacci que deseas generar: "))

if n > 1:
    resultado = fibonacci(n)
    print(f"Los primeros {n} números de la sucesión de Fibonacci son: {resultado}")
    
    
    k = random.randint(1, n)  

numero_secreto = resultado[k-1]  
intento = None

while intento != numero_secreto:
    intento = int(input("Adivina el número : "))
    if intento < numero_secreto:
            print("Muy bajo.")
    elif intento > numero_secreto:
            print("Muy alto.")
    else:
            print(f"¡Haz adivinado el número!: {numero_secreto}")