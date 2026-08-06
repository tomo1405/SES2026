import pytest
from src_0030 import task_func
import numpy as np

def test_task_func():
    data = np.array([[1, 2, 3], [4, 5, 6]])
    expected_output = "[[-1.22474487, -0.4472136, 0.9486833], [-0.9486833, -0.4472136, -1.22474487]]"
    assert task_func(data) == expected_output