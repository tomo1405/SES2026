python
import pandas as pd
import pytest
from src_0878 import task_func

def test_task_func():
    # Test case 1: Valid input
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_components = 2
    expected_result = pd.DataFrame({'PC1': [-0.70710678, -0.70710678], 'PC2': [0.70710678, 0.70710678]})
    result = task_func(data, n_components)
    assert result.equals(expected_result)

    # Test case 2: Invalid input: data is not a DataFrame
    data = [1, 2, 3]
    n_components = 2
    with pytest.raises(ValueError):
        task_func(data, n_components)

    # Test case 3: Invalid input: data contains non-numeric values
    data = pd.DataFrame({'A': [1, 2, 'a'], 'B': [4, 5, 6]})
    n_components = 2
    with pytest.raises(ValueError):
        task_func(data, n_components)

    # Test case 4: Invalid input: n_components is greater than the number of columns in data
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    n_components = 3
    with pytest.raises(ValueError):
        task_func(data, n_components)