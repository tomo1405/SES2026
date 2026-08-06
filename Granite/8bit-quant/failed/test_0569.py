import inspect
import matplotlib.pyplot as plt
import pandas as pd
import pytest

from src_0569 import task_func

def test_task_func():
    f_list = [lambda x: x, lambda x, y: x + y]
    with pytest.raises(ValueError):
        task_func(f_list)

def test_task_func_with_valid_functions():
    f_list = [lambda x: x, lambda x, y, z: x + y + z]
    df = task_func(f_list)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert df.index.tolist() == ['<lambda>', '<lambda>']
    assert df.columns.tolist() == ['Function Name', 'Number of Arguments']