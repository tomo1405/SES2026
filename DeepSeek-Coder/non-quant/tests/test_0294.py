import pytest
from src_0294 import task_func
import itertools
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    elements = [1, 2, 3, 4]
    subset_size = 2
    expected_combinations = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    expected_sums = [3, 4, 5, 5, 6, 7]

    result_gca, result_combinations, result_sums = task_func(elements, subset_size)

    assert result_combinations == expected_combinations
    assert result_sums == expected_sums

    # Additional assertions to check the plot (not implemented here due to complexity)