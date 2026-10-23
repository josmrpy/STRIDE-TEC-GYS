# Elaborado por: Josimar (solitario)
# Fecha de creación: 22/10/2026 08:40
# Fecha de finalización: 22/10/2026 08:46
# Versión 3.14.7

# Definicion de funciones
def crearSucesionUlam(num: int):
    sucesion = []
    # Hasta llegar a 1
    while num > 1:
        sucesion.append(num)
        if num % 2 == 0:  # par
            num = num // 2
        else:  # impar
            num = (num * 3) + 1
    # Se agrega el 1 por aparte
    sucesion.append(1)
    return sucesion

def crearListasUlam(valores: list):
    listasUlam = []
    for i in valores:
        sucesionUlam = crearSucesionUlam(i)
        listasUlam.append(sucesionUlam)
    return listasUlam

def recorrerLista(lista: list):
    for sublista in lista:
        print(sublista)

# Programa principal
misUlams = crearListasUlam([26, 13, 80])
recorrerLista(misUlams)
