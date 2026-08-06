import numpy as np
from itertools import chain
def task_func(L):
    flattened = list(chain.from_iterable(L))
    mean = np.mean(flattened)
    variance = np.var(flattened)
    
    return {'mean': mean, 'variance': variance}