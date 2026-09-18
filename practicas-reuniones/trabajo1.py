# Elaborado por Angeles, Enrique, Josimar (alfabeticamente)
# Fecha de creación: 17-09-2026 08:48
# Version 3.14
# Programa principal

# Pedir al estudiante que ingrese su matricula y 5 calificaciones (Entrada de datos)
mat = int(input("Ingrese la matrícula del estudiante: "))
cal1 = float(input("Ingrese la primera calificación: "))
cal2 = float(input("Ingrese la segunda calificación: "))
cal3 = float(input("Ingrese la tercera calificación: "))
cal4 = float(input("Ingrese la cuarta calificación: "))
cal5 = float(input("Ingrese la quinta calificación: "))

# promedio de las calificaciones (operación)
pro = (cal1 + cal2 + cal3 + cal4 + cal5) / 5

# determinar si el promedio es aprobado o no (primera condicion)
if pro >= 6:
    print(mat, pro, "Aprobado")
else:
    print(mat, pro, "No aprobado")
