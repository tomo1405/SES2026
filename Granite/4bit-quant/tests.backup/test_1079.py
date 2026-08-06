import pytest
from src_1079 import task_func
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Test with a uniform distribution
    arr = np.array([1, 2, 3, 4, 5])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == True
    assert ax.get_xticks().tolist() == [0, 1, 2, 3, 4]
    assert ax.get_xticklabels().tolist() == [1, 2, 3, 4, 5]

    # Test case 2: Test with a non-uniform distribution
    arr = np.array([1, 2, 2, 3, 3, 3])
    uniform_distribution, ax = task_func(arr)
    assert uniform_distribution == False
    assert ax.get_xticks().tolist() == [0, 1, 2, 3]
    assert ax.get_xticklabels().tolist() == [1, 2, 3, 3]

if __name__ == "__main__":
    pytest.main()