import pytest
from src_1079 import task_func
import numpy as np
import matplotlib.pyplot as plt

class TestTaskFunc:
    def test_uniform_distribution(self):
        arr = np.array([1, 2, 3, 4, 5])
        uniform_distribution, _ = task_func(arr)
        assert uniform_distribution == True

    def test_non_uniform_distribution(self):
        arr = np.array([1, 2, 2, 3, 4])
        uniform_distribution, _ = task_func(arr)
        assert uniform_distribution == False

    def test_plot(self):
        arr = np.array([1, 2, 3, 4, 5])
        _, ax = task_func(arr)
        assert ax.get_xticks().tolist() == [0, 1, 2, 3, 4]
        assert ax.get_xticklabels().tolist() == [1, 2, 3, 4, 5]