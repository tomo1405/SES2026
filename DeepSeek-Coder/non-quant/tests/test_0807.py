import pytest
from src_0807 import task_func

# Test cases for task_func

def test_task_func():
    # Test case 1: Basic functionality
    text = "This is a test. This test is only a test."
    result = task_func(text=text, n=2)
    assert result == {'This is': 1, 'is a': 1, 'a test': 2, 'test. This': 1}

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()