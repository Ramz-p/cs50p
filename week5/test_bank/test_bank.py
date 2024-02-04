# test_bank.py
from bank import value

def test_starts_with_hello():
    assert value("hello, world") == 0
    assert value("Hello, everyone!") == 0
    assert value("HELLO") == 0

def test_starts_with_h():
    assert value("hola") == 20
    assert value("H") == 20
    assert value("house") == 20

def test_otherwise():
    assert value("python") == 100
    assert value("c++") == 100
    assert value("Goodbye") == 100
