# Elaborado por Angeles, Enrique, Josimar (alfabeticamente)
# Fecha de creación: 17-09-2026 08:54
# Version 3.14
# Programa principal

# Pedir al usuario un numero entero (entrada de datos)
num = int(input("Ingrese el numero: "))

# evaluar si el numero es mayor a 0, si es positivo (primer condicional)
if num > 0:
    print("positivo")
else:
    # evaluar si el numero es igual a cero, de lo contrario es negativo (doble condicional)
    if num == 0:
        print("nulo")
    else:
        print("negativo")