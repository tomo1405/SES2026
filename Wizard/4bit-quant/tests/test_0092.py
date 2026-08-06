python
import pandas as pd
import pytest
from src_0092 import task_func

def test_task_func():
    # Test case 1: valid input
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column1 = 'A'
    column2 = 'B'
    expected_output = ((1.0, 0.0, 1.0, 0.0, 0.0), None)
    assert task_func(data, column1, column2) == expected_output

    # Test case 2: invalid column name
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column1 = 'C'
    column2 = 'D'
    with pytest.raises(ValueError):
        task_func(data, column1, column2)

    # Test case 3: missing column
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    column1 = 'A'
    column2 = 'C'
    with pytest.raises(ValueError):
        task_func(data, column1, column2)