import pytest
from src_0359 import task_func

# Test cases
def test_task_func():
    # Test case 1: Basic test
    json_list = '{"number_list": [1, 2, 3, 4]}'
    r = 2
    expected_output = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    assert task_func(json_list, r) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()