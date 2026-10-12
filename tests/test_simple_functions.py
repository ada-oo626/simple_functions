import pytest
from simple_functions import my_sum, sinx
from math import factorial
import numpy as np

class TestSimpleFunctions:
    """Tests for the functions in functions1.py."""

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4),
    ])
    def test_my_sum(self, iterable, expected):
        """my_sum adds up the items of lists and tuples."""
        assert my_sum(iterable) == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1),
        (0, 1),
    ])
    def test_factorial(self, number, expected):
        """factorial is right for small numbers, including 0! = 1."""
        assert factorial(number) == expected

    @pytest.mark.parametrize('number, expected', [
        (0, 0),
        (np.pi/4, 0.70710678),
        (np.pi/2, 1),
        (np.pi, 0),
    ])
    def test_sin(self, number, expected):
        assert sinx(number) == pytest.approx(expected, abs=1e-06)