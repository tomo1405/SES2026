import numpy as np
import pandas as pd
import random
def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    random.seed(seed)
    if min_val == max_val:
        matrix = np.full((rows, cols), min_val)
    else:
        matrix = np.array([[random.randrange(min_val, max_val) for j in range(cols)] for i in range(rows)])
    df = pd.DataFrame(matrix)
    return df