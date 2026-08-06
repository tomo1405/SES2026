import pytest
from src_1111 import task_func

def test_task_func():
    # Test case 1: Basic functionality
    word_dict = {'a': ['apple', 'banana'], 'b': ['banana'], 'c': ['apple']}
    expected_output = {'a': 2, 'b': 1, 'c': 1}
    assert task_func(word_dict) == expected_output

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()