################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejemplo1 import suma_digitos, signo


"""
Estos son los test correspondienets al archivo `ejemplo_1.py` que estan en
`src`
Idealmente, los tests van de los mas general, hacia lo mas especifico en
relacion a los resultados.

Con la terminal de Thonny en la raiz del proyecto, el archivo `test.py`
se encarga de ejecutar los tests con pytest (que es lo que el robot hará
luego)
"""


def test_suma_digitos_positivos():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 1234
    resultado = suma_digitos(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado >= 0, "El resultado debe ser mayor o igual que cero"
    assert resultado == 10, "No obtenemos el resultado esperado"


def test_suma_digitos_negativos():
    numero = -1234
    resultado = suma_digitos(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado <= 0, "El resultado debe ser menor o igual que cero"
    assert resultado == -10, "No obtenemos el resultado esperado"


def test_signo_positivo():
    numero = 10
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == 1, "el resultado para el valor 0, debe ser 0"


def test_signo_cero():
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == 0, "el resultado para el valor 0, debe ser 0"


def test_signo_negativo():
    numero = -10
    resultado = signo(numero)
    assert isinstance(resultado, int), "el resultado debe ser un número entero"
    assert resultado == -1, "el resultado para el valor 0, debe ser 0"
