import pytest
from src_0448 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def data():
    return np.array([[1, 2], [3, 4], [5, 6]])

def test_task_func(data):
    result = task_func(data)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert isinstance(result["ax"], plt.Axes)
    assert result["transformed_data"].shape == (3, 2)

def test_task_func_plot(data):
    result = task_func(data)
    assert plt.gcf().get_axes()