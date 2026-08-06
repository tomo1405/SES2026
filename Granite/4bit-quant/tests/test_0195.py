import numpy as np
from src_0195 import task_func


def test_task_func():
    data_size = 100
    data, color = task_func(data_size)
    assert isinstance(data, np.ndarray)
    assert isinstance(color, str)
    assert len(data) == data_size
    assert color in BAR_COLOR