import pytest
from src_0878 import task_func
import pandas as pd

def test_task_func():
    # Test case 1: Basic functionality
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = task_func(data)
    assert isinstance(result, pd.DataFrame), "The result should be a DataFrame"
    assert result.shape == (3, 2), "The result should have the correct shape"

    # Test case 2: Handling non-numeric data
    data = pd.DataFrame({
        'A': [1, 2, 'a'],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="DataFrame should only contain numeric values."):
        task_func(data)

    # Test case 3: Invalid n_components
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    with pytest.raises(ValueError, match="n_components should not be greater than the number of columns in data."):
        task_func(data, n_components=5)

    # Test case 4: Correct usage
    data = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    result = task_func(data, n_components=1)
    assert result.shape == (3, 1), "The result should have the correct shape with n_components=1"