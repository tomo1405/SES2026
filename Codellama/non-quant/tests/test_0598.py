import pandas as pd
from src_0598 import task_func


def test_task_func():
    data = [
        {'Name': 'John Doe', 'Age': 32},
        {'Name': 'Jane Doe', 'Age': 27},
        {'Name': 'John Smith', 'Age': 45},
        {'Name': 'Jane Smith', 'Age': 38},
        {'Name': 'John Johnson', 'Age': 52},
        {'Name': 'Jane Johnson', 'Age': 45}
    ]
    letter = 'j'
    expected_result = pd.DataFrame({'Name': ['John Doe', 'John Smith', 'John Johnson'], 'Age': [32, 45, 52]})
    result = task_func(data, letter)
    assert result.equals(expected_result)