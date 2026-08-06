import pandas as pd
from src_0559 import task_func


def test_task_func():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected_df = pd.DataFrame({
        'A': [-1.22474487, 0.0, 1.22474487],
        'B': [-1.22474487, 0.0, 1.22474487]
    })
    expected_ax = expected_df.plot(kind='bar')

    df, ax = task_func(a, b)

    assert df.equals(expected_df)
    assert ax == expected_ax

def test_task_func_empty_input():
    a = []
    b = []
    expected_df = pd.DataFrame()
    expected_ax = expected_df.plot(kind='bar')

    df, ax = task_func(a, b)

    assert df.equals(expected_df)
    assert ax == expected_ax