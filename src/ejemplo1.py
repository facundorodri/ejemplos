################
# Nombre - @martinvilu
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
A partir de un número entero.
Diseñar un algoritmo que permita mostrar la suma de los dígitos del número ingresado considerando el signo.
"""


def signo(numero):
    """
    Devuelve un número entero en relación con el signo del número indicado
        -1 negativo
        0 cero
        1 positivo
    """

    if numero > 0:
        sgn = 1
    elif numero < 0:
        sgn = -1
    else:
        sgn = 0
    return sgn


def suma_digitos(numero):
    """
    Calcula la suma de los dígitos del número ingresado considerando el signo
    Por ejemplo: -521 = 5 + 2 + 1 = -8
    """
    sgn = signo(numero)
    numero = abs(numero)
    suma = 0
    while numero > 0:
        digito = numero % 10
        cociente = numero // 10
        suma = suma + digito
        numero = cociente
    suma = suma * sgn
    return suma


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    un_numero = int(input("Ingrese un número entero para sumar sus dígitos: "))
    suma = suma_digitos(un_numero)
    print(f"la suma de los dígitos de {un_numero} es {suma}")


if __name__ == "__main__":
    principal()
