import numpy as np
import random
from scipy import stats
def task_func(list_of_lists, size=5, seed=0):
    random.seed(seed)
    data = []
    for list_ in list_of_lists:
        if list_:
            data += list_
        else:
            data += [random.randint(0, 100) for _ in range(size)]
    
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': stats.mode(data)[0]
    }