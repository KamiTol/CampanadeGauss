import math;

import matplotlib.pyplot as plt

def calcular_media_mediana():
    numero = input("Por favor, ingrese un número de 6 dígitos: ")
    cadena = str(numero)

    if len(cadena) != 6:
        return "El número debe tener 6 dígitos", []

    digitos = [int(digito) for digito in cadena]

    media = sum(digitos) / len(digitos)

    digitos.sort()
    if len(digitos) % 2 == 0:
        mediana = (digitos[len(digitos) // 2 - 1] + digitos[len(digitos) // 2]) / 2
    else:
        mediana = digitos[len(digitos) // 2]

    return media, mediana

def generar_pseudoaleatorios():
    semilla = input("Por favor, ingrese una semilla de 7 dígitos: ")
    if len(semilla) != 7:
        return "La semilla debe tener 7 dígitos", []

    numeros = []
    for _ in range(2000):
        cuadrado = str(int(semilla) ** 2)
        inicio = (len(cuadrado) - 7) // 2
        semilla = cuadrado[inicio:inicio + 7]
        semilla = semilla.zfill(7)
        numeros.append(int(semilla))

    return numeros

def calcular_operacionZ1(numeros_pseudoaleatorios):
    resultados = []
    for i in range(0, len(numeros_pseudoaleatorios), 2):
        U1 = numeros_pseudoaleatorios[i] / 10000000
        U2 = numeros_pseudoaleatorios[i+1] / 10000000

        resultado = math.sqrt(-2 * math.log(U1)) * math.cos(2 * math.pi * U2)
        resultados.append(resultado)

    return resultados

def calcular_normal(media, mediana, Z1):
    return mediana * Z1 + media

media, mediana = calcular_media_mediana()

numeros_pseudoaleatorios = generar_pseudoaleatorios()

Z1 = calcular_operacionZ1(numeros_pseudoaleatorios)

normales = [calcular_normal(media, mediana, z1) for z1 in Z1]

def graficar_normales(normales):
    # Crear el histograma normalizado (curva de campana de Gauss)
    plt.hist(normales, bins=30, density=True)

    # Mostrar el histograma
    plt.show()

# Llamar al método para graficar las normales
graficar_normales(normales)







