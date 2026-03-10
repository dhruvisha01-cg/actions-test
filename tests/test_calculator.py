"""Basic pytest tests for the calculator module."""

import pytest

from calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for add()."""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_add_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5


class TestSubtract:
    """Tests for subtract()."""

    def test_subtract_positive(self):
        assert subtract(10, 3) == 7

    def test_subtract_negative_result(self):
        assert subtract(2, 5) == -3


class TestMultiply:
    """Tests for multiply()."""

    def test_multiply_positive(self):
        assert multiply(4, 5) == 20

    def test_multiply_by_zero(self):
        assert multiply(100, 0) == 0


class TestDivide:
    """Tests for divide()."""

    def test_divide_normal(self):
        assert divide(10, 2) == 5.0

    def test_divide_raises_on_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(1, 0)
