import pytest
from src_0804 import task_func
import pandas as pd

def test_task_func_with_valid_input():
    file_name = "data.csv"
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df.to_csv(file_name, index=False)

    result = task_func(file_name)

    assert result.equals(pd.DataFrame({"A": [0.5, 1, 1.5], "B": [0.75, 1, 1.25]}))

def test_task_func_with_invalid_input():
    file_name = "data.csv"
    df = pd.DataFrame({"A": ["a", "b", "c"], "B": ["d", "e", "f"]})
    df.to_csv(file_name, index=False)

    with pytest.raises(ValueError):
        task_func(file_name)