from bank import value

def test_zero():
    assert value("Hello") == 0

def test_twenty():
    assert value("Hamburger") == 20

def test_one_hundred():
    assert value("Charlie") == 100
