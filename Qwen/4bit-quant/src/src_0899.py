from collections import Counter
import random
LETTERS = ['a', 'b', 'c', 'd', 'e']
def task_func(count, seed=0):
    random.seed(seed)

    pairs = [tuple(random.choices(LETTERS, k=2)) for _ in range(count)]
    pair_frequency = Counter(pairs)

    return pair_frequency