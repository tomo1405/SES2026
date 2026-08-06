import numpy as np
from src_0790 import task_func


def test_task_func():
    # Mock the constants
    global ARRAY_LENGTH
    ARRAY_LENGTH = 10

    # Call the function and store the result
    result = task_func()

    # Assert the expected result
    expected_result = array = np.random.randint(0, 10, ARRAY_LENGTH).reshape(-1, 1)
    scaler = MinMaxScaler()
    expected_result = scaler.fit_transform(expected_result)
    assert result.all() == expected_result.all()