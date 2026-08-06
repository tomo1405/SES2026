import pandas as pd
import pytest
from src_0092 import task_func


def test_task_func():
    data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column1 = 'A'
    column2 = 'B'

    slope, intercept, r_value, p_value, std_err = task_func(data, column1, column2)

    assert slope == 1.0
    assert intercept == 0.0
    assert r_value == 1.0
    assert p_value == 0.0
    assert std_err == 0.0

def test_task_func_invalid_columns():
    data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
    column1 = 'C'
    column2 = 'D'

    with pytest.raises(ValueError):
        task_func(data, column1, column2)