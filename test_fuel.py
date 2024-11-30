import pytest
from fuel import convert, gauge

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("2/1")