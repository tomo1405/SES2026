python
import numpy as np
import pandas as pd
import pytest

def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, len(columns))), columns=columns)
    df = df.drop(df.columns[remove_cols], axis=1)

    return df

def test_task_func():
    # Test case 1: n_rows is an integer
    assert isinstance(task_func(10, [0, 1, 2]), pd.DataFrame)

    # Test case 2: remove_cols is a list of integers
    assert isinstance(task_func(10, [0, 1, 2]), pd.DataFrame)

    # Test case 3: columns is a list of strings
    assert isinstance(task_func(10, [0, 1, 2]), pd.DataFrame)

    # Test case 4: random_seed is an integer
    assert isinstance(task_func(10, [0, 1, 2], random_seed=42), pd.DataFrame)

    # Test case 5: n_rows is a float
    with pytest.raises(TypeError):
        task_func(10.5, [0, 1, 2])

    # Test case 6: remove_cols is a list of floats
    with pytest.raises(TypeError):
        task_func(10, [0.5, 1.5, 2.5])

    # Test case 7: columns is a list of integers
    with pytest.raises(TypeError):
        task_func(10, [0, 1, 2], columns=[1, 2, 3, 4, 5])

    # Test case 8: random_seed is a float
    with pytest.raises(TypeError):
        task_func(10, [0, 1, 2], random_seed=42.5)

    # Test case 9: n_rows is a negative integer
    with pytest.raises(ValueError):
        task_func(-10, [0, 1, 2])

    # Test case 10: remove_cols is an empty list
    with pytest.raises(ValueError):
        task_func(10, [])

    # Test case 11: remove_cols is a list with duplicates
    with pytest.raises(ValueError):
        task_func(10, [0, 1, 2, 1])

    # Test case 12: remove_cols is a list with out-of-range indices
    with pytest.raises(ValueError):
        task_func(10, [0, 1, 20])

    # Test case 13: remove_cols is a list with negative indices
    with pytest.raises(ValueError):
        task_func(10, [0, -1, 2])

    # Test case 14: remove_cols is a list with non-integer indices
    with pytest.raises(TypeError):
        task_func(10, [0, '1', 2])