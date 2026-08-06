import pytest
import math
import pandas as pd
from src_0693 import task_func

@pytest.fixture
def tuples_list():
    return [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

def test_task_func(tuples_list):
    df = task_func(tuples_list)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert df.columns[0] == 0

def test_task_func_empty_list(tuples_list):
    df = task_func([])
    assert df.empty

def test_task_func_invalid_input(tuples_list):
    with pytest.raises(TypeError):
        task_func("invalid input")