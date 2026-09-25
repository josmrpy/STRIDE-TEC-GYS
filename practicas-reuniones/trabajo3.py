# Elaborado por: Josimar, Isaac, Sebas
# Fecha de creación: 18/9/2026 07:33
# Fecha de finalización: 18/9/2026 07:48
# Versión 3.14

# Programa principal, (habia que pasar a diagrama de flujo
print("""Calculadora super eficiente pythonica: Isaac, Josimar, Sebas
    1: suma
    2: resta
    3: multiplicacion
    4: division
""")
opera = int(input("Ingrese la operación a utilizar: "))
a = float(input("Ingrese el primer valor a calcular: "))
b = float(input("Ingrese el segundo valor a calcular: "))

match opera:
    case 1:  # Suma
        val = a + b
    case 2:  # Resta
        val = a - b
    case 3:  # Multiplicación
        val = a * b
    case 4:  # División
        val = a / b
    case _:  # NADA
        val = 0

print(val)
