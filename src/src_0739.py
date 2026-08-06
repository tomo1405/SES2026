import numpy as np
from scipy.stats import iqr
def task_func(L):
    flattened = np.array(L).flatten()
    iqr_value = iqr(flattened)
    
    return iqr_value