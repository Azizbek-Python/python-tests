import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Дополнительные тесты для расширенного покрытия
def test_add_negative():
    assert add(-1, -2) == -3

def test_divide_float():
    assert divide(5, 2) == 2.5

def test_multiply_by_zero():
    assert multiply(7, 0) == 0

def test_large_numbers():
    assert multiply(10**6, 10**6) == 10**12

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (-1, -1, -2),
    (0, 5, 5),
])
def test_add_param(a, b, result):
    assert add(a, b) == result
