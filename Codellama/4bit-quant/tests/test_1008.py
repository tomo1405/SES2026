import pandas as pd
import pytest
from src_1008 import task_func


def test_task_func():
    # Test case 1: Valid URL
    url = "https://api.example.com/data"
    expected_df = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]})
    actual_df = task_func(url)
    assert actual_df.equals(expected_df)

    # Test case 2: Invalid URL
    url = "https://api.example.com/data/invalid"
    with pytest.raises(SystemError):
        task_func(url)

    # Test case 3: Invalid JSON format
    url = "https://api.example.com/data/invalid_json"
    with pytest.raises(ValueError):
        task_func(url)