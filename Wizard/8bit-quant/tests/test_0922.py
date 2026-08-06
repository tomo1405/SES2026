python
import pandas as pd
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0922 import task_func

def test_task_func():
    # Test case 1: Normal case
    data = [[1, 2, 3], [4, 5, 6]]
    columns = ['col1', 'col2', 'col3']
    expected_result = [[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]]
    result = task_func(data, columns)
    assert result.values.tolist() == expected_result

    # Test case 2: Empty columns list
    data = [[1, 2, 3], [4, 5, 6]]
    columns = []
    expected_result = [[1, 2, 3], [4, 5, 6]]
    result = task_func(data, columns)
    assert result.values.tolist() == expected_result

    # Test case 3: Non-existent column name
    data = [[1, 2, 3], [4, 5, 6]]
    columns = ['col1', 'col2', 'col4']
    expected_result = [[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]]
    result = task_func(data, columns)
    assert result.values.tolist() == expected_result

    # Test case 4: Non-numeric data
    data = [[1, 2, 'a'], [4, 5, 'b']]
    columns = ['col1', 'col2', 'col3']
    expected_result = [[0.0, 0.0, 0.0], [1.0, 1.0, 1.0]]
    result = task_func(data, columns)
    assert result.values.tolist() == expected_result

    # Test case 5: Non-list data
    data = (1, 2, 3)
    columns = ['col1', 'col2', 'col3']
    with pytest.raises(TypeError):
        task_func(data, columns)

    # Test case 6: Non-list columns
    data = [[1, 2, 3], [4, 5, 6]]
    columns = 'col1'
    with pytest.raises(TypeError):
        task_func(data, columns)