from bank import value

def test_hello():
    assert value("hello") == 0

def test_comeca_h():
    assert value("Halksjçlkd") == 20

def test_nao_comeca_h():
    lista_letras_sem_h = "qwertyuiopasdfgjklzxcvbnm"
    for letra in lista_letras_sem_h:
        assert value(letra) == 100
