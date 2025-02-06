import seasons
from seasons import formato_valido
from seasons import dia_valido
from seasons import mes_valido

def test_formato_valido():
    assert formato_valido(r"1988-08-30") == (1988,8,30)
    assert formato_valido(r"1988-12-31") == (1988,12,31)
    assert formato_valido(r"1988-01-1") == (1988,1,1)

def test_dia_valido_true():
    assert dia_valido(1,1) is True
    assert dia_valido(1,12) is True
    assert dia_valido(31,12) is True

def test_dia_valido_false():
    assert dia_valido(32,1) is False
    assert dia_valido(1,13) is False
    assert dia_valido(0,15) is False

def test_mes_valido():
    assert mes_valido(1) is True
    assert mes_valido(12) is True
    assert mes_valido(13) is False


