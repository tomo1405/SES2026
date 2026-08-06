import pytest
from src_0804 import task_func
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Test case 1: Normal case
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    result = task_func(df=df)
    assert result.equals(df)

    # Test case 2: No numeric columns
    data = {
        'A': ['a', 'b', 'c'],
        'B': ['d', 'e', 'f']
    }
    df = pd.DataFrame(data)
    with pytest.raises(ValueError):
        task_func(df=df)

    # Test case 3: Normal case with scaling
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    result = task_func(df=df)
    assert result.equals(df)