import numpy as np
from scipy import stats
def task_func(L):
    flattened = np.hstack(L)  
    mode = stats.mode(flattened)[0][0]
    return mode