import pandas as pd
import matplotlib.pyplot as plt
from random import randint
from src_0166 import task_func
import pytest

@pytest.mark.parametrize("num_rows, rand_range, expected_output", [
    (5, (0, 100), plt.Figure),
    (10, (10, 20), plt.Figure),
    (2, (50, 100), plt.Figure),
])
def test_task_func(num_rows, rand_range, expected_output):
    output = task_func(num_rows, rand_range)
    assert isinstance(output, expected_output)