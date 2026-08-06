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
    assert task_func([1, 2, 3, 4, 5]) == 1.6094379124341005
    assert task_func([1, 2, 3, 4, 5, 6]) == 1.791759469228055
    assert task_func([1, 2, 3, 4, 5, 6, 7]) == 1.9459101490553132
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8]) == 2.0794415416798357
    assert task_func([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2.1972245773362196