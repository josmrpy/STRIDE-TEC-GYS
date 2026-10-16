# Elaborado por: Josimar y la mitad de la clase
# Fecha de creación: 15/10/2026 08:27
# Fecha de finalización: 15/10/2026 08:30
# Versión 3.14.7

# Importacion de librerias

#Definicion de funciones

#Programa principal, Solo es copiar el codigo de la imagen
clave = input("Ingrese su clave: ")
indice = 0
while indice < len(clave):
    letra = clave[indice]
    print("la letra de la posición ", indice, "es: ", letra)
    indice += 1
print("el largo de la clave es: ", len(clave))