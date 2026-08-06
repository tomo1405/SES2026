import pytest
from src_1048 import task_func
from datetime import datetime
import random
import matplotlib.pyplot as plt

def test_task_func():
    date_str = "2023-01-01"
    ax = task_func(date_str)
    assert ax is not None
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_date_str():
    date_str = "2023-02-30"
    with pytest.raises(ValueError):
        task_func(date_str)

def test_task_func_with_invalid_input_type():
    with pytest.raises(TypeError):
        task_func(123)