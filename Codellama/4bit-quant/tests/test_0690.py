import pandas as pd
import pytest
from src_0690 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    p_values = task_func(df)
    assert p_values['A'] > 0.05
    assert p_values['B'] > 0.05

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(None)