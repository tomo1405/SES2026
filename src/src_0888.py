import pandas as pd
import numpy as np
import itertools
def task_func(T1, row_num=50, seed=None):
    np.random.seed(seed)
    int_list = [list(map(int, x)) for x in T1]
    flattened_list = list(itertools.chain(*int_list))
    total_cols = sum(flattened_list)

    data = np.random.randint(0, 100, size=(row_num, total_cols))
    df = pd.DataFrame(data, columns=[f'Col_{i+1}' for i in range(total_cols)])

    return df