def mostrar_pasos(matriz_aumentada):
    """Función para mostrar la matriz aumentada en cada paso con 4 decimales"""
    print("\nMatriz aumentada actual:")
    # Mostrar la matriz redondeada a 4 decimales sin mostrar np.float64
    for fila in matriz_aumentada:
        print([round(float(elem), 4) for elem in fila])

def gauss_jordan_ordenado(matriz, b):
    """Función que resuelve un sistema de ecuaciones lineales usando el método de Gauss-Jordan en el orden dado"""
    # Crear la matriz aumentada
    matriz_aumentada = np.hstack([matriz, b.reshape(-1, 1)])
    mostrar_pasos(matriz_aumentada)

    # Hacer el pivote en la posición (1,1) igual a 1
    print("\nPaso 1: Hacemos que el pivote en (1,1) sea 1 dividiendo toda la fila 1 por", round(matriz_aumentada[0][0], 4))
    matriz_aumentada[0] = matriz_aumentada[0] / matriz_aumentada[0][0]
    mostrar_pasos(matriz_aumentada)

    # Hacer 0 en (2,1) y (3,1)
    print("\nPaso 2: Hacemos 0 en la posición (2,1) restando", round(matriz_aumentada[1][0], 4), "veces la fila 1 de la fila 2")
    matriz_aumentada[1] = matriz_aumentada[1] - matriz_aumentada[1][0] * matriz_aumentada[0]
    mostrar_pasos(matriz_aumentada)

    print("\nPaso 3: Hacemos 0 en la posición (3,1) restando", round(matriz_aumentada[2][0], 4), "veces la fila 1 de la fila 3")
    matriz_aumentada[2] = matriz_aumentada[2] - matriz_aumentada[2][0] * matriz_aumentada[0]
    mostrar_pasos(matriz_aumentada)

    # Hacer el pivote en la posición (2,2) igual a 1
    print("\nPaso 4: Hacemos que el pivote en (2,2) sea 1 dividiendo toda la fila 2 por", round(matriz_aumentada[1][1], 4))
    matriz_aumentada[1] = matriz_aumentada[1] / matriz_aumentada[1][1]
    mostrar_pasos(matriz_aumentada)

    # Hacer 0 en la posición (3,2)
    print("\nPaso 5: Hacemos 0 en la posición (3,2) restando", round(matriz_aumentada[2][1], 4), "veces la fila 2 de la fila 3")
    matriz_aumentada[2] = matriz_aumentada[2] - matriz_aumentada[2][1] * matriz_aumentada[1]
    mostrar_pasos(matriz_aumentada)

    # Hacer el pivote en la posición (3,3) igual a 1
    print("\nPaso 6: Hacemos que el pivote en (3,3) sea 1 dividiendo toda la fila 3 por", round(matriz_aumentada[2][2], 4))
    matriz_aumentada[2] = matriz_aumentada[2] / matriz_aumentada[2][2]
    mostrar_pasos(matriz_aumentada)

    # Hacer 0 en la posición (2,3)
    print("\nPaso 7: Hacemos 0 en la posición (2,3) restando", round(matriz_aumentada[1][2], 4), "veces la fila 3 de la fila 2")
    matriz_aumentada[1] = matriz_aumentada[1] - matriz_aumentada[1][2] * matriz_aumentada[2]
    mostrar_pasos(matriz_aumentada)

    # Hacer 0 en la posición (1,3)
    print("\nPaso 8: Hacemos 0 en la posición (1,3) restando", round(matriz_aumentada[0][2], 4), "veces la fila 3 de la fila 1")
    matriz_aumentada[0] = matriz_aumentada[0] - matriz_aumentada[0][2] * matriz_aumentada[2]
    mostrar_pasos(matriz_aumentada)

    # Hacer 0 en la posición (1,2)
    print("\nPaso 9: Hacemos 0 en la posición (1,2) restando", round(matriz_aumentada[0][1], 4), "veces la fila 2 de la fila 1")
    matriz_aumentada[0] = matriz_aumentada[0] - matriz_aumentada[0][1] * matriz_aumentada[1]
    mostrar_pasos(matriz_aumentada)

    # Paso final: Las soluciones están en la última columna de la matriz aumentada
    soluciones = matriz_aumentada[:, -1]
    return soluciones

def main():
    print("Ingrese los valores de la matriz 3x3:")
    
    # Definir una matriz 3x3
    matriz = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            matriz[i][j] = float(input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))

    # Definir el vector b
    b = np.array([float(input(f"Ingrese el valor de b{i+1}: ")) for i in range(3)])

    print("\nLa matriz ingresada es:\n", matriz)
    print("\nEl vector b es:\n", b)

    # Resolver usando Gauss-Jordan en el orden especificado
    soluciones = gauss_jordan_ordenado(matriz, b)

    # Mostrar la solución final
    print("\nLa solución del sistema es:")
    print(f"x = {round(soluciones[0], 4)}")
    print(f"y = {round(soluciones[1], 4)}")
    print(f"z = {round(soluciones[2], 4)}")

if __name__ == "__main__":
    main()