import pandas as pd
import pytest
from src_0798 import task_func


def test_task_func():
    df = pd.DataFrame({'A': ['(a)', '(b)'], 'B': ['(c)', '(d)']})
    assert task_func(df) == 4

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func(1)

def test_task_func_invalid_input_type():
    df = pd.DataFrame({'A': ['(a)', '(b)'], 'B': ['(c)', '(d)']})
    with pytest.raises(TypeError):
        task_func(df, 1)