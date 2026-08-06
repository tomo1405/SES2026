import pytest
from src_0222 import task_func
import numpy as np
import pandas as pd

# Define test cases
def test_task_func():
    # Test case 1: Basic functionality
    data = {
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [5, 4, 3, 2, 1],
        'feature3': [1, 3, 2, 5, 4],
        'feature4': [2, 3, 4, 1, 5],
        'feature5': [5, 1, 2, 3, 4]
    }
    df = pd.DataFrame(data)
    dct = {}
    result = task_func(df, dct)
    assert result == {
        'feature1': {'mean': 3.0, 'median': 3.0, 'mode': 1, 'variance': 2.5},
        'feature2': {'mean': 3.0, 'median': 3.0, 'mode': 1, 'variance': 2.5},
        'feature3': {'mean': 3.0, 'median': 3.0, 'mode': 1, 'variance': 2.5},
        'feature4': {'mean': 3.0, 'median': 3.0, 'mode': 1, 'variance': 2.5},
        'feature5': {'mean': 3.0, 'median': 3.0, 'mode': 1, 'variance': 2.5}
    }

if __name__ == "__main__":
    pytest.main()