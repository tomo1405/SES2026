import numpy as np
import random
def task_func(length=10000, seed=0):
    if length < 0:
        raise ValueError("length must be a non-negative integer")
    random.seed(seed)
    steps = [1 if random.random() > 0.5 else -1 for _ in range(length)]
    walk = np.cumsum([0] + steps)  # Starts at 0
    return walk