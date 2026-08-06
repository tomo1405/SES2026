import pandas as pd
import pytest
from src_0141 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    cols = ['A', 'B']
    expected_output = pd.DataFrame({'A': [0, 0, 0], 'B': [0, 0, 0]})

    output = task_func(df, cols)

    assert isinstance(output, pd.DataFrame)
    assert output.equals(expected_output)

def test_task_func_invalid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    cols = ['A', 'B', 'C']

    with pytest.raises(ValueError):
        task_func(df, cols)