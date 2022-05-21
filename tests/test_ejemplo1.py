################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejemplo1 import suma_digitos, signo


"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_suma_digitos_positivos():
    """
       Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 1234
    resultado = suma_digitos(numero)
    assert resultado == 10, "No obtenemos el resultado esperado"

def test_suma_digitos_negativos():
    numero = -1234
    resultado = suma_digitos(numero)
    assert resultado == -10, "No obtenemos el resultado esperado"
    
def test_signo_positivo():
    numero = 10
    resultado = signo(numero)
    assert resultado == 1

def test_signo_cero():
    numero = 0
    resultado = signo(numero)
    assert resultado == 0
    
def test_signo_negativo():
    numero = -10
    resultado = signo(numero)
    assert resultado == -1
