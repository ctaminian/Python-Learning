from numb3rs import validate

def test_valid_ipv4():
    assert validate("192.168.1.1") == True

def test_invalid_ipv4():
    assert validate("260.1.2.3") == False