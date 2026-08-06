import pytest
from src_1089 import task_func
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1: Test with default data
    expected_output = pd.DataFrame({'A': [0, 0, 0, 0, 0], 'B': [0, 0, 0, 0, 0], 'C': [0, 0, 0, 0, 0], 'D': [0, 0, 0, 0, 0], 'E': [0, 0, 0, 0, 0]})
    output = task_func()
    assert np.allclose(output, expected_output)

    # Test case 2: Test with custom data
    data = np.array([[0.1, 0.2, 0.3, 0.4, 0.5], [0.6, 0.7, 0.8, 0.9, 1.0]])
    expected_output = pd.DataFrame({'A': [0.1, 0.2], 'B': [0.3, 0.4], 'C': [0.5, 0.6], 'D': [0.7, 0.8], 'E': [0.9, 1.0]})
    output = task_func(data)
    assert np.allclose(output, expected_output)

    # Test case 3: Test with invalid data
    data = np.array([[0.1, 0.2, 0.3, 0.4, 0.5], [0.6, 0.7, 0.8, 0.9, 1.1]])
    with pytest.raises(ValueError):
        task_func(data)