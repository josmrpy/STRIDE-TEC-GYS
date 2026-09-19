# Elaborado por: Josimar Madrigal
# Fecha de creación: 18/9/2026 01:00
# Fecha de finalización: 18/9/2026 01:06
# Versión 3.14

# Programa principal, problema 2.9
prebas = float(input("Ingrese el precio base: "))  # Entrada de datos
if prebas > 500:  # primer condicional
    imp = 20 * 0.30 + (prebas - 40) * 0.50
elif prebas > 40:  # segundo condicional
    imp = 20 * 0.30 + (prebas - 40) * 0.40
elif prebas > 20:  # tercer condicional
    imp = (prebas - 20) * 0.30
else:
    imp = 0
pretot = prebas + imp
print(prebas, pretot)
