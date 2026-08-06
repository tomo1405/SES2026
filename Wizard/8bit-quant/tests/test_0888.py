python
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

def test_task_func():
    T1 = [['1', '2', '3'], ['4', '5', '6']]
    df = task_func(T1, seed=42)
    assert df.shape == (50, 9)
    assert df.columns.tolist() == ['Col_1', 'Col_2', 'Col_3', 'Col_4', 'Col_5', 'Col_6', 'Col_7', 'Col_8', 'Col_9']
    assert df.iloc[0].tolist() == [31, 10, 11, 10, 10, 10, 10, 10, 10]
    assert df.iloc[49].tolist() == [31, 10, 11, 10, 10, 10, 10, 10, 10]

test_task_func()