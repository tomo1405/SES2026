import pytest
from src_0984 import task_func
import pandas as pd
import numpy as np
import seaborn as sns

# Test cases for task_func

def test_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_non_numeric_data():
    data = {
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    }
    df = pd.DataFrame(data)
    with pytest.raises(TypeError):
        task_func(df)

def test_valid_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)
    result = task_func(df)
    assert isinstance(result[0], pd.DataFrame)
    assert isinstance(result[1], sns.axisgrid.PairGrid)