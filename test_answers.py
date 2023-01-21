from answers import brute_force, two_pointers, numpy_subtract
import pytest


@pytest.mark.parametrize("a,b,expected", [
    ([47, 24, 95, 184, 13, 3, 12, 18], [83, 9, 32, 29, 52, 90, 108, 14], 1),
    ([2, 56, -8, 100, -2], [2, 56, -8, 100, -2], 0),
    ([2, -8, -9, 0, 100], [101, 8, 22, 4], 1)
])
def test_approaches(a, b, expected):
    assert brute_force(a, b) == expected
    assert two_pointers(a, b) == expected
    assert numpy_subtract(a, b) == expected
