import numpy as np

def resolver_matriz(matriz):
    """Función para resolver una matriz utilizando numpy."""
    try:
        # Intentamos calcular la inversa de la matriz
        inversa = np.linalg.inv(matriz)
        print("La inversa de la matriz es:\n", inversa)
        
        # Para matrices de la forma Ax = b, resolvemos
        b = np.array([float(input("Ingrese el valor de b{}: ".format(i + 1))) for i in range(matriz.shape[0])])
        x = np.dot(inversa, b)
        
        # Presentación de resultados
        if matriz.shape[0] == 2:
            print(f"La solución del sistema es:\n x = {x[0]}\n y = {x[1]}")
        elif matriz.shape[0] == 3:
            print(f"La solución del sistema es:\n x = {x[0]}\n y = {x[1]}\n z = {x[2]}")
            
    except np.linalg.LinAlgError:
        print("La matriz no es invertible. Verifica los valores ingresados.")

def main():
    print("Selecciona el tamaño de la matriz:")
    print("1. Matriz 2x2")
    print("2. Matriz 3x3")
    
    opcion = input("Ingrese 1 o 2: ")

    if opcion == '1':
        # Definir una matriz 2x2
        matriz = np.zeros((2, 2))
        print("Ingrese los valores de la matriz 2x2:")
        
        for i in range(2):
            for j in range(2):
                matriz[i][j] = float(input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))
        
        print("La matriz ingresada es:\n", matriz)
        resolver_matriz(matriz)

    elif opcion == '2':
        # Definir una matriz 3x3
        matriz = np.zeros((3, 3))
        print("Ingrese los valores de la matriz 3x3:")
        
        for i in range(3):
            for j in range(3):
                matriz[i][j] = float(input(f"Ingrese el valor de la posición ({i+1},{j+1}): "))
        
        print("La matriz ingresada es:\n", matriz)
        resolver_matriz(matriz)

    else:
        print("Opción no válida. Por favor elija 1 o 2.")

if __name__ == "__main__":
    main()