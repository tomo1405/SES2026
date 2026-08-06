import pytest
from src_0873 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [4.0, 5.0, 7.0]
    assert task_func(data_list=data_list) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()