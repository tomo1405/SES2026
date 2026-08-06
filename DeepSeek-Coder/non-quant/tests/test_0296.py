import pytest
from src_0296 import task_func

# Test cases for the function
def test_task_func():
    # Test case 1: Basic test
    elements = [1, 2, 3]
    subset_size = 2
    expected = {
        'mean': 3.0,
        'median': 3.0,
        'mode': 3
    }
    assert task_func(elements, subset_size) == expected

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()