from um import count

def test_count_qtde():
    assert count(r"!um, tá ok") == 1
    assert count(r"um um uma") == 2

def test_count_zero():
    assert count(r"entendi, ok então") == 0
    assert count(r"entendi, ummmm, ok então") == 0
    assert count(r"a mumia") == 0

def test_count_ignorecase():
    assert count(r"UM entendi") == 1
    assert count(r"UM UM UMMMM, entendi") == 2
    assert count(r"UM um um UMMMM ummmm, entendi") == 3


