import itertools
import math
from pandas import Series
def task_func(elements, subset_size, top_n=2):
    if subset_size > len(elements) or subset_size <= 0:
        return 1, []

    combinations = list(itertools.combinations(elements, subset_size))
    sums = [sum(combination) for combination in combinations if len(combination) != 0]
    product = math.prod(sums)
    top_sums = sorted(sums, reverse=True)[:top_n]
    top_sums = Series(top_sums)
    return product, top_sums