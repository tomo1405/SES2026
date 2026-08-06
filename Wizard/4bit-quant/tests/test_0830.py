python
import pandas as pd
import pytest
from src_0830 import task_func

def test_task_func():
    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [80, 70, 90]})
    result_dict = task_func(df)
    assert result_dict == {'Alice': [('Alice', 80.0)], 'Bob': [('Bob', 70.0)], 'Charlie': [('Charlie', 90.0)]}

    df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Score': [80, 70, 90], 'Age': [25, 30, 40]})
    with pytest.raises(ValueError):
        task_func(df)