from twttr import shorten

def test_shorten_so_vogais():
    assert shorten("aeiouAEIOU") == ""

def test_shorten_so_consoantes():
    assert shorten("QWRTYPSDFGHJKLZXCVBNM") == "QWRTYPSDFGHJKLZXCVBNM"
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"

def test_shorten_misturado():
    assert shorten("fernando santos barbosa") == "frnnd snts brbs"

def test_shorten_numeros():
    assert shorten("1234567890") == "1234567890"

def test_shorten_pontuacao():
    assert shorten(",.;:´`!@#$%¨&*()") == ",.;:´`!@#$%¨&*()"

