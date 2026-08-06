import pytest
from src_0557 import task_func

# Define test cases
def test_task_func():
    # Test case 1
    s = "example"
    min_length = 5
    max_length = 10
    letters = "abc"
    result = task_func(s, min_length, max_length, letters)
    assert isinstance(result, tuple)
    assert len(result[0]) >= min_length and len(result[0]) <= max_length
    assert isinstance(result[1], bool)

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()