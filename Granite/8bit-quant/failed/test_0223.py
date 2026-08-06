import pytest
import math
import numpy as np
import matplotlib.pyplot as plt
from src_0223 import task_func

def test_task_func():
    list_input = [math.pi, math.e, math.sqrt(2)]
    cumsum, ax = task_func(list_input)
    assert isinstance(cumsum, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

def test_task_func_with_negative_numbers():
    list_input = [-math.pi, -math.e, -math.sqrt(2)]
    cumsum, ax = task_func(list_input)
    assert isinstance(cumsum, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

def test_task_func_with_zero():
    list_input = [0]
    cumsum, ax = task_func(list_input)
    assert isinstance(cumsum, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Cumulative Sum Plot"
    assert ax.get_xlabel() == "Index"
    assert ax.get_ylabel() == "Cumulative Sum"

def test_task_func_with_empty_list():
    list_input = []
    with pytest.raises(ValueError):
        cumsum, ax = task_func(list_input)