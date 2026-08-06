import pytest
from src_0138 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    skewness = task_func(df)
    assert skewness == 0.0

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(None)

def test_task_func_empty_input():
    df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_non_numeric_input():
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_nan_input():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df.iloc[0, 0] = np.nan
    skewness = task_func(df)
    assert skewness == 0.0