# Elaborado por: Josimar Madrigal
# Fecha de creación: 11/10/2026 1:27
# Fecha de finalización: 11/10/2026 1:30
# Versión 3.14.7

# Programa principal, DF 2.16 : meter en una función
def temperatura(n):
    if n > 0:
        t = n / 4 + 40
        print("Temperatura", t)
n = int(input("Ingrese un numero (n): "))
temperatura(n)