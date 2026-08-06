python
import pandas as pd
import numpy as np
import pytest
from sklearn.preprocessing import StandardScaler
from src_0681 import task_func

def test_task_func():
    # Test case 1: empty features list
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    features = []
    expected = df
    actual = task_func(df, features)
    assert actual.equals(expected)

    # Test case 2: valid features list
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    features = ['A', 'B']
    expected = pd.DataFrame({'A': [-1.3416407864998738, 0., 1.3416407864998738], 'B': [-1.3416407864998738, 0., 1.3416407864998738]}, index=[0, 1, 2])
    actual = task_func(df, features)
    assert actual.equals(expected)

    # Test case 3: invalid features list (non-existent column)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    features = ['A', 'D']
    with pytest.raises(KeyError):
        task_func(df, features)

    # Test case 4: invalid features list (empty list)
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    features = []
    with pytest.raises(ValueError):
        task_func(df, features)