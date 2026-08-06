import pytest
from src_0738 import task_func

def test_task_func():
    # Test case 1: Normal case
    assert task_func([[1, 2, [3, 4, [5, 6]], 7]) == 4.0

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()