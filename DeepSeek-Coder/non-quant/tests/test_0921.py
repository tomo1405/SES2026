import pytest
from src_0921 import task_func
import pandas as pd
import seaborn as sns

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6]
    }
    result = task_func(data)
    assert result is not None