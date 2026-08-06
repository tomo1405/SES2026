import pytest
from src_0606 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def matrix():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_task_func(matrix):
    ax = task_func(matrix)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_input(matrix):
    with pytest.raises(ValueError):
        task_func("invalid input")

def test_task_func_with_empty_matrix(matrix):
    empty_matrix = []
    with pytest.raises(ValueError):
        task_func(empty_matrix)