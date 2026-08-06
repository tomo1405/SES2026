python
import pytest
from src_0190 import task_func

def test_task_func():
    # Test case 1: Valid input
    data_url = "https://jsonplaceholder.typicode.com/users"
    expected_output = ['Bret', 'Antonette', 'Samantha', 'Gabriel', 'David', 'Emma']
    assert task_func(data_url) == expected_output

    # Test case 2: Invalid input
    data_url = "https://jsonplaceholder.typicode.com/invalid_url"
    expected_output = "Invalid url input"
    assert task_func(data_url) == expected_output