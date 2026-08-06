import pytest
from src_0114 import task_func
import json
from collections import Counter
import random

# Test cases
def test_task_func():
    # Test with valid input
    my_dict = {}
    keys = list(range(10))
    result = task_func(my_dict, keys)
    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], dict)
    assert isinstance(result[1], str)
    assert isinstance(result[2], str)

    # Add more assertions to check the content and behavior of the function

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()