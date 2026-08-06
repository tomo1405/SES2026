from functools import reduce
from itertools import combinations
import numpy as np
def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if seed is not None:
        np.random.seed(seed)

    if high <= low:
        raise ValueError("The 'high' parameter must be greater than 'low'.")

    matrix = np.random.randint(low, high, shape)
    values = matrix.flatten()

    all_pairs = list(combinations(values, 2))

    sum_of_products = reduce(lambda a, b: a + b, [np.prod(pair) for pair in all_pairs])

    return sum_of_products, matrix