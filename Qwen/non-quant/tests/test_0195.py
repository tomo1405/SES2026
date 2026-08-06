import numpy as np
from src_0195 import task_func


def test_task_func_data_size():
    data_size = 10
    data, color = task_func(data_size)
    assert len(data) == data_size, "The length of the data array does not match the input data size."

def test_task_func_color():
    data_size = 10
    data, color = task_func(data_size)
    assert color in BAR_COLOR, "The selected color is not in the predefined list of colors."

def test_task_func_data_distribution():
    data_size = 1000
    data, color = task_func(data_size)
    assert np.allclose(np.mean(data), 0, atol=0.1), "The mean of the data is not close to 0."
    assert np.allclose(np.std(data), 1, atol=0.1), "The standard deviation of the data is not close to 1."

def test_task_func_reproducibility():
    data_size = 10
    data1, color1 = task_func(data_size)
    data2, color2 = task_func(data_size)
    assert np.array_equal(data1, data2), "The data generated with the same seed is not reproducible."
    assert color1 == color2, "The color selected with the same seed is not reproducible."