import random
import numpy as np
from numpy.linalg import solve

#Ejercicio 1
def divisores(num):
    return [i for i in range(1, num) if num % i == 0]

n = int(input("Ingresa un número entero: "))

divs = divisores(n)
print(f"Los divisores de {n} (excluyendo el propio número) son: {divs}")
#----------------------------------------------------------------------------
#Ejercicio 2
def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return 366
    else:
        return 365

año = int(input("Ingresa un año: "))
print(f"El año {año} tiene {año_bisiesto(año)} días.")
#---------------------------------------------------------------------------
#Ejercicio 3
def sumatorio_diferencias(lista):
    return sum(lista[i] - lista[i-1] for i in range(1, len(lista)))

numeros = input("Ingresa los números separados por comas: ")
lista = [int(num) for num in numeros.split(",")]

print("El sumatorio de las diferencias es:", sumatorio_diferencias(lista))
#----------------------------------------------------------------------------
#Ejercicio 4
def cadena_mas_larga(cadenas):
    return max(cadenas, key=len)

cadenas_input = input("Ingresa las cadenas separadas por comas: ")
cadenas = [cadena.strip() for cadena in cadenas_input.split(",")]

print("La cadena más larga es:", cadena_mas_larga(cadenas))
#-----------------------------------------------------------------------------
#Ejercicio 5
def numero_aleatorio():
    return random.uniform(0.0, 10.0)

print(numero_aleatorio())
#-----------------------------------------------------------------------------
#Ejercicio 6
def dado():
    return random.randint(1, 6)

print(dado())
#-----------------------------------------------------------------------------
#Ejercicio 7
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def muestra_primos(n):
    primos = []
    for i in range(1, n + 1):
        if es_primo(i):
            primos.append(i)
    return primos

n = int(input("Ingresa un número: "))

if es_primo(n):
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")

primos = muestra_primos(n)
print(f"Los números primos entre 1 y {n} son: {primos}")

#-----------------------------------------------------------------------------
#Ejercicio 8

def suma_diagonal(matriz):
    if len(matriz) == len(matriz[0]):
        return sum(matriz[i][i] for i in range(len(matriz)))
    else:
        return None

n = int(input("Ingresa el tamaño de la matriz cuadrada (por ejemplo, 2 para una matriz 2x2, 3 para una matriz 3x3, etc.): "))

numeros = []
print(f"Ingresa los números para una matriz {n}x{n} uno por uno:")
for i in range(n*n):
    num = int(input(f"Ingresa el número {i+1}: "))
    numeros.append(num)

matriz = np.array(numeros).reshape(n, n)

print("\nMatriz ingresada:")
print(matriz)

print("\nLa suma de la diagonal principal es:", suma_diagonal(matriz))
#-----------------------------------------------------------------------------
#Ejercicio 9
def matriz_diagonal(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matriz[i][i] = 1
    matriz[0][n-1] = matriz[n-1][0] = -20
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

n = 5
matriz = matriz_diagonal(n)
imprimir_matriz(matriz)
#-----------------------------------------------------------------------------
#Ejercicio 10

# Parte a)
A1 = np.array([[3, 4], [-2, -3]])
b1 = np.array([-1, 2])
solucion1 = solve(A1, b1)
print("Solución parte a):", solucion1)

# Parte b)
A2 = np.array([[4, 1, 0, 0], [1, 4, 1, 0], [0, 1, 4, 1], [0, 0, 1, 3]])
b2 = np.array([15, 10, 10, 10])
solucion2 = solve(A2, b2)
print("Solución parte b):", solucion2)

