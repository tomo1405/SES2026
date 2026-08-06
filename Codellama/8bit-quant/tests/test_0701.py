import pytest
from src_0701 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    data = [[1, 2], [3, 4]]
    cols = ['a', 'b']
    expected_result = pd.DataFrame([[1, 0], [0, 1]], columns=cols)
    result = task_func(data, cols)
    assert np.allclose(result, expected_result)