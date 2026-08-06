python
import pandas as pd
import pytest
from src_0237 import task_func

def test_task_func():
    # Test case 1: Test with valid input
    df = pd.DataFrame({'Name': ['John', 'Mary', 'John', 'Peter'], 'Age': [25, 30, 28, 35], 'Score': [85, 90, 88, 95], 'Category': ['A', 'B', 'A', 'C']})
    assert task_func(df) == 0.5
    
    # Test case 2: Test with invalid input
    with pytest.raises(ValueError):
        task_func(123)