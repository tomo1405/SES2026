import pytest
from src_0210 import task_func
import numpy as np

def test_task_func():
    data = [(1, 2), (3, 4), (5, 6)]
    ax = task_func(data)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Max Tuple Highlighted'
    assert ax.get_legend() == 'Data'
    assert ax.get_legend() == 'Max Tuple'
    assert ax.get_legend().get_color() == 'red'
    assert ax.get_legend().get_label() == 'Max Tuple'