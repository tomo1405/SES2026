python
import math
import itertools
from functools import reduce

def task_func(numbers):
    sum_log_products = 0

    for r in range(1, len(numbers) + 1):
        combinations = itertools.combinations(numbers, r)
        for combination in combinations:
            product = reduce(lambda x, y: x * y, combination)
            sum_log_products += math.log(product)

    return sum_log_products

def test_task_func():
    assert task_func([1, 2, 3, 4, 5]) == 10.451369234883384
    assert task_func([1, 2, 3, 4, 5, 6]) == 11.098612288668109
    assert task_func([1, 2, 3, 4, 5, 6, 7]) == 11.718281828459045