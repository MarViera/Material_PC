# Pruebas automatizadas con pytest
from funciones import validar_puerto, es_ip_privada

def test_puerto_valido():
    assert validar_puerto(80) == True

def test_puerto_invalido_cero():
    assert validar_puerto(0) == False

def test_puerto_invalido_alto():
    assert validar_puerto(99999) == False

def test_ip_privada_correcta():
    assert es_ip_privada("192.168.1.1") == True

def test_ip_publica():
    assert es_ip_privada("8.8.8.8") == False
