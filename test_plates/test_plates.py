import plates

def test_inicia_2_letras():
    assert plates.is_valid("aa") == True
    assert plates.is_valid("a2") == False
    assert plates.is_valid("2a") == False
    assert plates.is_valid("22") == False

def test_num_por_ultimo():
    assert plates.is_valid("ajssk2") == True
    assert plates.is_valid("ajs2k2") == False
    assert plates.is_valid("2jssk2") == False

def test_entre_2e6():
    for i in range(2,7):
        placa = "a" * i
        assert plates.is_valid(placa) == True

def test_tamamnho_incorreto():
    assert plates.is_valid("aaaaaaa") == False
    assert plates.is_valid("a") == False

def test_first_num_not_zero():
    assert plates.is_valid("aasd20") == True
    assert plates.is_valid("0asdfg") == False
    assert plates.is_valid("aasd02") == False

def test_somente_alphanum():
    lista_pontuacao = "!@#$%¨&*()_+,.;/?:><"
    for pontuacao in lista_pontuacao:
        placa = "aaaa" + pontuacao
        assert plates.is_valid(placa) == False

