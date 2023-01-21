from random import randint

import pytest

from answers import brute_force, numpy_subtract, two_pointers


@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([47, 24, 95, 184, 13, 3, 12, 18], [83, 9, 32, 29, 52, 90, 108, 14], 1),
        ([2, 56, -8, 100, -2], [2, 56, -8, 100, -2], 0),
        ([2, -8, -9, 0, 100], [101, 8, 22, 4], 1),
    ],
)
def test_approaches(a, b, expected):
    assert brute_force(a, b) == expected
    assert two_pointers(a, b) == expected
    assert numpy_subtract(a, b) == expected


# use module scope so we get the same inputs for each benchmark
@pytest.fixture(scope="module")
def input_arrs():
    a = [randint(1, 10e6) for _ in range(1000)]
    b = [randint(1, 10e6) for _ in range(1000)]
    return a, b


def test_brute_force_bench(benchmark, input_arrs):
    benchmark(brute_force, *input_arrs)


def test_two_pointers_bench(benchmark, input_arrs):
    benchmark(two_pointers, *input_arrs)


def test_numpy_subtract_bench(benchmark, input_arrs):
    benchmark(numpy_subtract, *input_arrs)
