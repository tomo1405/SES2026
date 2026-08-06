import numpy as np
import pandas as pd
def task_func(rows, columns, seed=None):
    if seed is not None:
        np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    df = pd.DataFrame(matrix)
    
    return df