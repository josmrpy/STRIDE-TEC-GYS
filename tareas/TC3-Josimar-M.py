# Elaborado por: Josimar Madrigal
# Fecha de creación: 24/9/2026 09:12
# Fecha de finalización: 24/9/2026 09:23
# Versión 3.14

# Programa principal, DF 2.27
sueldo = float(input("Ingrese el sueldo: "))
categoria = int(input("Ingrese la categoría: "))
horasExtras = int(input("Ingrese las horas extras: "))

# condicional multiple
if categoria == 1:
    precioHorasExtra = 30
elif categoria == 2:
    precioHorasExtra = 38
elif categoria == 3:
    precioHorasExtra = 50
elif categoria == 4:
    precioHorasExtra = 70
else:
    precioHorasExtra = 0

# condicional simple
if horasExtras > 30:
    numeroSueldo = sueldo + 30 * precioHorasExtra
else:
    numeroSueldo = sueldo + horasExtras * precioHorasExtra

print(numeroSueldo)
