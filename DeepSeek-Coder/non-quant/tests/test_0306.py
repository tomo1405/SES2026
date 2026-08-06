import pytest
from src_0306 import task_func

# Test cases for task_func

def test_task_func():
    # Test case 1: Basic functionality
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1})
    assert task_func(list_of_lists) == expected_output

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()