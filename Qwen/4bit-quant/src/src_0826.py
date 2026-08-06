import numpy as np
from itertools import product
import string
def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    np.random.seed(seed)
    all_combinations = [''.join(p) for p in product(alphabets, repeat=length)]
    return np.random.choice(all_combinations, size=10).tolist()