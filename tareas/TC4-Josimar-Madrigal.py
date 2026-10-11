# Elaborado por: Josimar Madrigal
# Fecha de creación: 8/10/2026 6:00
# Fecha de finalización: 8/10/2026 6:10
# Versión 3.14

# Programa principal, DF 3.14
# Inicialización de variables
med = 0
chi = 0
gra = 0
n = int(input("Ingrese la cantidad de datos: "))
i = 1
# Ciclo while
while i <= n:
    v = float(input(f"Ingrese el valor {i}: "))
    # Condicional multiple
    if v <= 200:
        chi = chi + 1
    elif v < 400:
        med = med + 1
    else:
        gra = gra + 1
    i = i + 1
# Mostrar resultados
print(chi, med, gra)
