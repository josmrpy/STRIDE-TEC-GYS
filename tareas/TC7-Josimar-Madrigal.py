# Elaborado por: Josimar, Ángeles
# Fecha de creación: 4/11/2026 09:20pm
# Fecha de finalización: 4/11/2026 10:22pm
# Versión 3.14.7

# * Definición de funciones
# (tratemos de no asumir que los numeros siempre van a ser diferentes, pueden haber varios iguales)
def recorrerMatriz(matriz: list, num: int):
    posiciones = []
    iFila = 0  # iterador de fila
    while iFila < len(matriz):
        iColumna = 0  # iterador de columna
        while iColumna < len(matriz[iFila]):
            campo = matriz[iFila][iColumna]
            if campo == num:
                posiciones.append([iFila, iColumna])
            iColumna += 1
        iFila += 1
    # al final, asumiendo que no habrá 0 coincidencias!!
    return posiciones

# Misma estructura, ignoremos que lo hago tres veces
def buscarMenorMayor(matriz: list):
    # Esto es para empezar con el primer valor de la matriz
    menor = matriz[0][0]
    mayor = menor
    iFila = 0
    while iFila < len(matriz):
        iColumna = 0
        while iColumna < len(matriz[iFila]):
            campo = matriz[iFila][iColumna]
            # si el nuevo es menor al actual
            if campo < menor:
                menor = campo
            # si el nuevo es mayor al actual
            if campo > mayor:
                mayor = campo
            iColumna += 1
        iFila += 1
    return menor, mayor

def analizarAula(matriz: list):
    menor, mayor = buscarMenorMayor(matriz)
    posMenor = recorrerMatriz(matriz, menor)
    posMayor = recorrerMatriz(matriz, mayor)
    # TODO: A partir de aquí, pensaba hacer una detección de si es singular o plural
    # pero me aburrí, así que solo hace for de las posiciones
    print("El alumno de menor edad está en la")
    for posicion in posMenor:
        print(f"Fila {posicion[0]}, columna {posicion[1]} y tiene {menor} año(s)")
    print("El alumno de mayor edad está en la")
    for posicion in posMayor:
        print(f"Fila {posicion[0]}, columna {posicion[1]} y tiene {mayor} año(s)")

# * Definición de variables
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = [[13, 12, 23, 14], [17, 25, 16, 15], [11, 18, 19, 21]]

# * Programa principal
analizarAula(matrix)
analizarAula(matriz)

"""Estructura while para recorrer matrices
i = 0
while i < len(matriz):
    j = 0
    while j < len(matriz):
        j += 1
    i += 1
"""
