python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0804 import task_func

def test_task_func():
    # Test case 1: Input file has no numeric columns
    df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 2: Input file has numeric columns
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    result = task_func(df)
    assert result.equals(pd.DataFrame({'A': [0.0, 0.5, 1.0], 'B': [0.0, 0.5, 1.0]}))

    # Test case 3: Input file has only one numeric column
    df = pd.DataFrame({'A': [1, 2, 3]})
    result = task_func(df)
    assert result.equals(pd.DataFrame({'A': [0.0, 0.5, 1.0]}))