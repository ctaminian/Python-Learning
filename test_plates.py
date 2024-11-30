from plates import is_valid

def test__max_length():
    assert is_valid("AAAAAA") == True

def test__min_length():
    assert is_valid("A") == False

def test__start_with_zero():
    assert is_valid("00AABB") == False

def test__no_middle_numbers():
    assert is_valid("AA00BB") == False