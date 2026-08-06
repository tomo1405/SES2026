import numpy as np
import matplotlib.pyplot as plt
from src_0442 import task_func

def test_task_func():
    P = np.array([[1, 2, 3], [4, 5, 6]])
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    expected_result = np.array([[50, 56, 62], [114, 136, 158]])
    expected_ax_shape = (1, 3)

    result, ax = task_func(P, T)

    assert np.array_equal(result, expected_result)
    assert ax.shape == expected_ax_shape

def test_task_func_invalid_inputs():
    P = [1, 2, 3]
    T = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

    with pytest.raises(TypeError):
        task_func(P, T)