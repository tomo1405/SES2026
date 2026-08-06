import random
import math
def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    random.seed(random_seed)
    pairs = [(random.randint(range_start, range_end), random.randint(range_start, range_end)) for _ in range(pairs_count)]
    return ((x, y, math.sqrt(abs(x - y))) for x, y in pairs)