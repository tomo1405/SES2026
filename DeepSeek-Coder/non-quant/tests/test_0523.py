import pytest
from src_0523 import task_func
import collections
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Basic functionality
    data = [
        {'Alice': 85, 'Bob': 72, 'Charlie': 90},
        {'Alice': 88, 'Bob': 75, 'Charlie': 92},
        {'Alice': 82, 'Bob': 78, 'Charlie': 95}
    ]
    result = task_func(data)
    assert result is not None

    # Add more assertions as needed to cover different scenarios

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()