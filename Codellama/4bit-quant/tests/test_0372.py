import pandas as pd
from src_0372 import task_func


def test_task_func():
    l = [1, 2, 3, 4, 5]
    expected_output = pd.DataFrame({'Scaled Values': [0.0, 0.5, 1.0, 1.5, 2.0]}, dtype=float)
    assert task_func(l).equals(expected_output)