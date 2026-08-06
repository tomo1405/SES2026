import pytest
from src_1116 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    input_dict = {'A': 2, 'B': 3}
    expected_output = [
        'AABCDE', 'AABCDF', 'AABCEF', 'AABCGF', 'AABCHF',
        'BAADEF', 'BAACDF', 'BAACEF', 'BAACGF', 'BAACHF'
    ]
    assert task_func(input_dict) == expected_output

    # Add more test cases as needed

# Add more test cases as needed