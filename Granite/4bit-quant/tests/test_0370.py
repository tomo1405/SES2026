import pytest
from src_0370 import task_func

def test_task_func():
    # Test case 1: Test with a list of numbers
    l = [1, 2, 3, 4, 5]
    ax = task_func(l)
    assert ax is not None
    # Add more assertions to test the output of the function

    # Test case 2: Test with an empty list
    l = []
    ax = task_func(l)
    assert ax is not None
    # Add more assertions to test the output of the function

    # Test case 3: Test with a list of strings
    l = ['a', 'b', 'c', 'd', 'e']
    ax = task_func(l)
    assert ax is not None
    # Add more assertions to test the output of the function

if __name__ == "__main__":
    pytest.main()