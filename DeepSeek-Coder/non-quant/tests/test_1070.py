import pytest
from src_1070 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Mock data for testing
data_dict = {
    'A': [1, 2, 2, 3, 3, 3],
    'B': [1, 1, 2, 2, 3, 3],
    'C': [1, 1, 1, 2, 2, 2]
}

def test_task_func():
    result = task_func(data_dict)
    assert isinstance(result, list), "The function should return a list of axes objects."
    assert all(isinstance(ax, plt.Axes) for ax in result), "Each element in the result should be an Axes object."
    assert len(result) == len(data_dict), "The number of axes objects should match the number of columns in the data."