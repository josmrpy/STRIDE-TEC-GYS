# Elaborado por: Josimar, Nahomi, Enrique
# Fecha de creación: 6/10/2026 08:25
# Fecha de finalización: 6/10/2026 08:35
# Versión 3.14

# Programa principal, diagrama 5.13
mayor = -100000
menor = 100000
n = int(input("Ingrese el numero de repiticiones: "))
i = 1  # iterador
# Inicio del ciclo
while i <= n:
    numero = float(input("Ingrese un numero: "))
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    i += 1
# Fin del ciclo
print(mayor, menor)
