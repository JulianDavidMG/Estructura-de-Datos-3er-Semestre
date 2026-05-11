import numpy as np

def mostrar_pasos(matriz_aumentada):
    """Función para mostrar la matriz aumentada en cada paso con 4 decimales, reemplazando -0 por 0 y separando la matriz de identidad."""
    print("\nMatriz aumentada actual:")
    n = matriz_aumentada.shape[1] // 2  # Tamaño de la matriz original
    for fila in matriz_aumentada:
        # Separamos la matriz original de la identidad con una línea divisoria
        original = [0 if abs(round(float(elem), 4)) == 0 else round(float(elem), 4) for elem in fila[:n]]
        identidad = [0 if abs(round(float(elem), 4)) == 0 else round(float(elem), 4) for elem in fila[n:]]
        print(original, "|", identidad)

def intercambiar_filas(matriz_aumentada, fila1, fila2):
    """Intercambia dos filas de la matriz aumentada"""
    matriz_aumentada[[fila1, fila2]] = matriz_aumentada[[fila2, fila1]]
    print(f"\nSe intercambian la fila {fila1+1} con la fila {fila2+1} para evitar un pivote cercano a cero.")
    mostrar_pasos(matriz_aumentada)

def gauss_jordan_inversa(matriz):
    """Función que calcula la inversa de una matriz usando el método de Gauss-Jordan con manejo de pivotes cero"""
    # Crear la matriz aumentada [A|I], donde I es la matriz identidad
    identidad = np.eye(matriz.shape[0])
    matriz_aumentada = np.hstack([matriz, identidad])
    mostrar_pasos(matriz_aumentada)

    n = matriz.shape[0]

    for i in range(n):
        # Si el pivote es cero o cercano a cero, buscar una fila para intercambiar
        if abs(matriz_aumentada[i][i]) < 1e-10:
            # Buscar otra fila con un pivote diferente de cero
            for k in range(i+1, n):
                if abs(matriz_aumentada[k][i]) > 1e-10:
                    intercambiar_filas(matriz_aumentada, i, k)
                    break
            else:
                # Si no se encuentra ninguna fila con un pivote diferente de cero
                print("La matriz no es invertible debido a un pivote cero.")
                return None

        # Hacer que el pivote sea 1
        print(f"\nPaso {i + 1}: Hacemos que el pivote en ({i+1},{i+1}) sea 1 ( / {round(matriz_aumentada[i][i], 4)})")
        matriz_aumentada[i] = matriz_aumentada[i] / matriz_aumentada[i][i]
        mostrar_pasos(matriz_aumentada)

        # Hacer 0 en las demás posiciones de la columna i
        for j in range(n):
            if i != j:
                print(f"\nPaso {i + 2}: Hacemos 0 en la posición ({j+1},{i+1}) ( - {round(matriz_aumentada[j][i], 4)} * fila {i+1})")
                matriz_aumentada[j] = matriz_aumentada[j] - matriz_aumentada[j][i] * matriz_aumentada[i]
                mostrar_pasos(matriz_aumentada)

    # Extraer la matriz inversa que está en la parte derecha de la matriz aumentada
    inversa = matriz_aumentada[:, n:]
    return inversa

def main():
    # Elegir el tamaño de la matriz
    while True:
        try:
            n = int(input("Elige el tamaño de la matriz (2 para 2x2, 3 para 3x3): "))
            if n not in [2, 3]:
                print("Por favor, elige 2 o 3.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Intenta de nuevo.")
    
    print(f"\nHas elegido una matriz de {n}x{n}. Ingrese los valores:")

    # Definir una matriz nxn
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matriz[i][j] = float(input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))

    print("\nLa matriz ingresada es:\n", matriz)

    # Verificar si la matriz es invertible (determinante distinto de 0)
    if np.linalg.det(matriz) == 0:
        print("La matriz no es invertible.")
    else:
        # Resolver usando Gauss-Jordan para encontrar la inversa
        inversa = gauss_jordan_inversa(matriz)

        if inversa is not None:
            # Mostrar la matriz inversa
            print("\nLa matriz inversa es:")
            print(inversa)

if __name__ == "__main__":
    main()  