import pandas as pd
from collections import Counter
from src_0680 import task_func
import pytest

@pytest.fixture
def input_df():
    return pd.DataFrame({'A': [1, 2, 2, 3], 'B': [2, 3, 4, 4]})

def test_task_func(input_df):
    result = task_func(input_df)
    assert isinstance(result, dict)
    assert len(result) == 3

def test_task_func_with_empty_df(input_df):
    input_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(input_df)

def test_task_func_with_non_df_input(input_df):
    with pytest.raises(TypeError):
        task_func([1, 2, 3])