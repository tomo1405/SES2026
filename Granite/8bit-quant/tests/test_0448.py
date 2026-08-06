import matplotlib.pyplot as plt
import numpy as np
from src_0448 import task_func


def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    result = task_func(data)
    assert "transformed_data" in result and "ax" in result
    assert isinstance(result["transformed_data"], np.ndarray)
    assert isinstance(result["ax"], plt.Axes)