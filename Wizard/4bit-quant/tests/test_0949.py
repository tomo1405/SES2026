python
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pytest

def task_func(rows=3, columns=2, seed=42):
    np.random.seed(seed) # Ensure reproducibility for consistent outputs across different runs
    matrix = np.random.rand(rows, columns)
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(matrix)

    return scaled_matrix

def test_task_func():
    # Test case 1: Test with default arguments
    assert task_func().shape == (3, 2)

    # Test case 2: Test with custom arguments
    assert task_func(rows=5, columns=4, seed=123).shape == (5, 4)

    # Test case 3: Test with invalid arguments
    with pytest.raises(TypeError):
        task_func(rows='3', columns=2, seed=42)