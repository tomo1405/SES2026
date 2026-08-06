import pytest
from src_0223 import task_func
import math
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def list_input():
    return [math.pi, math.e, math.sqrt(2), 1, 2, 3]

def test_task_func(list_input):
    cumsum, ax = task_func(list_input)
    assert isinstance(cumsum, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(cumsum) == len(list_input)
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

def test_task_func_with_negative_numbers(list_input):
    list_input.append(-1)
    with pytest.raises(ValueError):
        task_func(list_input)

def test_task_func_with_non_numeric_inputs(list_input):
    list_input.append("hello")
    with pytest.raises(TypeError):
        task_func(list_input)