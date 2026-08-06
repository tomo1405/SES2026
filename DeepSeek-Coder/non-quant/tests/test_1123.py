import pytest
from src_1123 import task_func

def test_task_func():
    # Test case 1: Basic URL
    result = task_func("Visit https://example.com for more information.")
    assert result == {'example.com': 'IP_ADDRESS'}

    # Add more test cases as needed