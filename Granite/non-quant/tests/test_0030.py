import numpy as np
import pytest
from src_0030 import task_func


def test_task_func():
    data = np.array([[1, 2], [3, 4], [5, 6]])
    expected_output = 'AXwBAgMEBQYHCAkKCwwNDg='
    actual_output = task_func(data)
    assert actual_output == expected_output

def test_task_func_with_invalid_input():
    data = 'invalid_input'
    with pytest.raises(TypeError):
        task_func(data)