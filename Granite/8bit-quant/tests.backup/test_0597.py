import pytest
from src_0597 import task_func

def test_task_func():
    duration = 5  # Set the desired duration for the test
    x_data, y_data = task_func(duration)

    assert len(x_data) > 0  # Check if x_data is not empty
    assert len(y_data) == len(x_data)  # Check if y_data has the same length as x_data
    assert all(isinstance(val, int) for val in y_data)  # Check if all values in y_data are integers
    assert all(val >= 0 and val <= 100 for val in y_data)  # Check if all values in y_data are within the specified range

    # Add more assertions as needed to cover the specific requirements of the function

if __name__ == "__main__":
    pytest.main()