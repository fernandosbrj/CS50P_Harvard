from lines import comentario, linha_em_branco


def test_comentario():
    assert comentario("#") is True
    assert comentario(" #") is True
    assert comentario("# ") is True
    assert comentario("abcd#") is False
    assert comentario("  #") is True

def test_linha_em_branco():
    assert linha_em_branco("") is True
    assert linha_em_branco("a") is False
