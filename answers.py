import itertools
from typing import List

import numpy as np


def brute_force(a: List[int], b: List[int]):
    ans = float("inf")
    for x, y in itertools.product(a, b):
        diff = abs(x - y)  # we only care about non-negative difference
        ans = min(ans, diff)
    return ans


def two_pointers(a: List[int], b: List[int]):
    a, b = sorted(a), sorted(b)
    i, j = 0, 0
    ans = float("inf")
    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])
        ans = min(ans, diff)
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans


def numpy_subtract(a: List[int], b: List[int]):
    a, b = np.array(a), np.array(b)
    diff_arr = np.subtract.outer(a, b)
    return np.absolute(diff_arr).min()
