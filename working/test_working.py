from working import convert
import pytest

def test_convert_valido():
    assert convert(r"9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert(r"9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert(r"9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert(r"9 AM to 5 PM") == "09:00 to 17:00"

def test_convert_invalido1():
    with pytest.raises(ValueError):
        convert(r"9:00 AM to")
        convert(r"to 5:00 PM")


def test_convert_invalido2():
    with pytest.raises(ValueError):
        convert(r"26 PM to 15 PM")
        convert(r"9:60 AM to 9:60 PM")

def test_convert_sem_to():
    with pytest.raises(ValueError):
        convert(r"9:00 AM 5 PM")

