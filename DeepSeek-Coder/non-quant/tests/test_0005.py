import pytest
from src_0005 import task_func
from collections import Counter
import itertools

def test_task_func():
    # Test case 1
    data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
    expected_output = {'1': 3, '2': 3, '3': 3, '4': 3, '5': 3, '6': 3}
    assert task_func(data) == expected_output

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()