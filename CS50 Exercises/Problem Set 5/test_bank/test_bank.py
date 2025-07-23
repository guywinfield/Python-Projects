from bank import value

def test_hello_0():
    assert value("hello") == 0
    assert value("hello, there friend") == 0
    assert value("HELLO") == 0
    assert value("hELLo there") == 0
    assert value("hello, Newman") == 0

def test_starts_h_20():
    assert value("howdy") == 20
    assert value("hey, there friend") == 20
    assert value ("hi") == 20

def test_no_h_100():
    assert value("gday") == 100
    assert value("Alright pal") == 100
    assert value ("sup") == 100

