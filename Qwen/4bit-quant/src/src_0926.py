import pandas as pd
import numpy as np
def task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0):
    np.random.seed(seed)
    df = pd.DataFrame(np.random.randint(1, 101, size=(data_size, len(column_names))), columns=column_names)
    df[df < 10] = -1  # Correctly replace values less than 10 with -1
    return df