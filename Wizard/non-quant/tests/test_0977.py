python
import numpy as np
import pandas as pd
import pytest
from sklearn.preprocessing import StandardScaler
from src_0977 import task_func

def test_task_func():
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    random_seed = 0
    expected_df = pd.DataFrame([[0.5764, -0.9569, -0.2241],
                                [-0.9569, -0.5764, 0.2241],
                                [0.2241, 0.9569, -0.5764]],
                               columns=['f1', 'f2', 'f3'])

    df = task_func(records, random_seed)

    assert df.equals(expected_df)

def test_task_func_with_random_seed():
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    random_seed = 1
    expected_df = pd.DataFrame([[-0.5764, 0.9569, 0.2241],
                                [0.9569, 0.5764, -0.2241],
                                [-0.2241, -0.9569, 0.5764]],
                               columns=['f1', 'f2', 'f3'])

    df = task_func(records, random_seed)

    assert df.equals(expected_df)

def test_task_func_with_invalid_input():
    records = np.array([1, 2, 3])
    random_seed = 0

    with pytest.raises(ValueError):
        task_func(records, random_seed)

def test_task_func_with_invalid_random_seed():
    records = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    random_seed = "invalid"

    with pytest.raises(ValueError):
        task_func(records, random_seed)