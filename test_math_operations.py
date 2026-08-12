# test_math_operations.py
import pytest
from math_operations import multiply, divide


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
