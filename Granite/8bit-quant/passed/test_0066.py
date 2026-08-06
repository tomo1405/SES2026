import pandas as pd
import matplotlib.pyplot as plt
import pytest
from src_0066 import task_func

def test_task_func():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_columns = ['col1', 'col2', 'col3']
    expected_nunique = [3, 3, 3]
    expected_xlabel = '-'.join(expected_columns[:-1])
    expected_ylabel = expected_columns[-1]

    df, ax = task_func(data)

    assert df.columns.tolist() == expected_columns
    assert df.nunique().tolist() == expected_nunique
    assert ax.get_xlabel() == expected_xlabel
    assert ax.get_ylabel() == expected_ylabel