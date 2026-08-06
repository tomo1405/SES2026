import numpy as np
from src_0790 import task_func


def test_task_func():
    # Test that the function returns a numpy array
    assert isinstance(task_func(), np.ndarray)

    # Test that the function returns an array with the correct shape
    assert task_func().shape == (ARRAY_LENGTH, 1)

    # Test that the function returns an array with values between 0 and 1
    assert np.all(task_func() >= 0) and np.all(task_func() <= 1)

    # Test that the function returns an array with the same values as the input array
    # after scaling
    array = np.random.randint(0, 10, ARRAY_LENGTH).reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(array)
    assert np.all(task_func() == scaled_array)