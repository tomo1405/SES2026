import pytest
from src_0364 import task_func

def test_task_func():
    # Test with valid input
    result = task_func([0, 1, 2, 3, 4])
    assert result == {0: 1, 1: 1, 2: 2, 3: 6, 4: 24}

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()