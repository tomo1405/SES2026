import numpy as np
from itertools import combinations
def task_func(n):

    if n < 1:
        raise ValueError("Input must be a positive integer")
    numbers = np.arange(1, n + 1)
    pairs = list(combinations(numbers, 2))
    return pairs