import pytest
from src_0977 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    expected_output = pd.DataFrame({"f1": [0.5, 0.5, 0.5], "f2": [0.5, 0.5, 0.5], "f3": [0.5, 0.5, 0.5]})
    output = task_func(records, random_seed)
    assert np.allclose(output, expected_output)

def test_task_func_random_seed():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 1
    expected_output = pd.DataFrame({"f1": [0.5, 0.5, 0.5], "f2": [0.5, 0.5, 0.5], "f3": [0.5, 0.5, 0.5]})
    output = task_func(records, random_seed)
    assert np.allclose(output, expected_output)

def test_task_func_invalid_input():
    records = np.array([[1, 2, 3], [4, 5, 6]])
    random_seed = 0
    with pytest.raises(ValueError):
        task_func(records, random_seed)