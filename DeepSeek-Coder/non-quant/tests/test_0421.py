import pytest
from src_0421 import task_func
import pandas as pd
from sklearn.preprocessing import StandardScaler

def test_task_func():
    # Test case 1: Basic functionality
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    }
    expected_output = pd.DataFrame({
        'A': [-1.0, 0.0, 1.0],
        'B': [-1.0, 0.0, 1.0],
        'C': [-1.0, 0.0, 1.0]
    })
    assert task_func(data)

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()