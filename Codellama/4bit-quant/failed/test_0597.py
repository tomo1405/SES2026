import pytest
from src_0597 import task_func

def test_task_func():
    # Test that the function returns a tuple of two lists
    x_data, y_data = task_func(10)
    assert isinstance(x_data, list)
    assert isinstance(y_data, list)

    # Test that the length of the lists is equal to the duration
    assert len(x_data) == 10
    assert len(y_data) == 10

    # Test that the values in the lists are within the expected range
    assert all(0 <= x <= 100 for x in x_data)
    assert all(0 <= y <= 100 for y in y_data)

    # Test that the function plots the data correctly
    # This test is not possible to implement without modifying the target code

if __name__ == '__main__':
    pytest.main()