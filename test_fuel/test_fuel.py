from fuel import convert, gauge
import pytest

# convert test functions

def test_convert():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100


def test_convert_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("8/0")

def test_convert_text_error():
    with pytest.raises(ValueError):
        convert("texto/ aaa")

def test_convert_numerador_maior():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_numerador_nao_inteiro():
    with pytest.raises(ValueError):
        convert("1.5/2")

def test_convert_denominador_nao_inteiro():
    with pytest.raises(ValueError):
        convert("2/4.5")

# gauge test functions

def test_gauge_E():
    assert gauge(0.99) == "E"
    assert gauge(1) == "E"

def test_gauge_parcial_cheio():
    assert gauge(1.00001) == "1.00001%"
    assert gauge(89.99999) == "89.99999%"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(99.01) == "F"


