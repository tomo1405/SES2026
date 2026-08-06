import pytest
from src_0312 import task_func

# Test cases for the function
def test_task_func():
    # Test case 1: Basic functionality
    result = task_func([[1, 2, 3], [4, 5, 6]])
    assert result == {
        'mean': 3.5,
        'median': 3.5,
        'mode': 1
    }

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()