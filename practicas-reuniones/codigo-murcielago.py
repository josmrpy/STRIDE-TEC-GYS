# Elaborado por: Josimar, Enrique, Juan, Angeles
# Fecha de creación: 15/10/2026 08:50
# Fecha de finalización: 15/10/2026 08:56
# Versión 3.14.7

# Programa principal, Hacer codigo murcielago

def traducirMurcielago(palabra):
    codigo = "MURCIELAGO"
    resultado = ""
    posicion = 0
    while posicion < len(palabra):
        letra = palabra[posicion].upper()
        numero = codigo.find(letra)
        if numero != -1:
            resultado += str(numero)
        else:
            resultado += letra
        posicion += 1
    return resultado
resultado = traducirMurcielago(input("Ingrese su palabra a convertir: "))
print("La palabra codificada es:", resultado)

#añadido personal: aprovechar .find para usar el -1