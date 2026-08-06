import pytest
from src_0597 import task_func

def test_task_func():
    duration = 5  # Set the desired duration for the test
    x_data, y_data = task_func(duration)

    assert len(x_data) > 0  # Check if x_data is not empty
    assert len(y_data) == len(x_data)  # Check if the lengths of x_data and y_data are equal
    assert all(isinstance(x, str) for x in x_data)  # Check if all elements in x_data are strings
    assert all(isinstance(y, int) for y in y_data)  # Check if all elements in y_data are integers
    assert all(0 <= y <= 100 for y in y_data)  # Check if all elements in y_data are within the specified range

    # Add more assertions as needed to cover the expected behavior of the function

if __name__ == "__main__":
    pytest.main()