import pytest
from src_0742 import task_func

# Test cases
def test_task_func():
    # Test case 1
    my_dict = {'a1': 10, 'a2': 20, 'b1': 30, 'b2': 40}
    expected_output = {'a': 30, 'b': 70}
    assert task_func(my_dict=my_dict) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()