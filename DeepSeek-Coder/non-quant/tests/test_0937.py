import pytest
from src_0937 import task_func
import numpy as np
import matplotlib.pyplot as plt
import string

def test_task_func_valid_input():
    word = "hello"
    result = task_func(word)
    assert result is not None

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func("hello1")

def test_task_func_plot():
    word = "hello"
    result = task_func(word)
    assert result is not None
    plt.close()