import numpy as np
import pandas as pd
import pytest
from src_0164 import task_func


def test_task_func_valid_input():
    rows = 5
    cols = 5
    expected_output = pd.DataFrame(np.random.rand(rows, cols) * 100, columns=['A', 'B', 'C', 'D', 'E'])
    actual_output = task_func(rows, cols)
    assert actual_output.equals(expected_output)

def test_task_func_invalid_input():
    rows = 5
    cols = 6
    with pytest.raises(ValueError):
        task_func(rows, cols)