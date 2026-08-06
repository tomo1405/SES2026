import pytest
from src_0808 import task_func
import numpy as np

def test_task_func():
    # Test case 1: No outliers
    data = np.array([1, 2, 3, 4, 5])
    outliers, mean, std_dev = task_func(data)
    assert outliers == []
    assert mean == 3
    assert std_dev == 1

    # Test case 2: With outliers
    data = np.array([1, 2, 3, 4, 5, 100])
    outliers, mean, std_dev = task_func(data)
    assert outliers == [4]
    assert mean == 3
    assert std_dev == 1

    # Test case 3: With multiple outliers
    data = np.array([1, 2, 3, 4, 5, 100, 200])
    outliers, mean, std_dev = task_func(data)
    assert outliers == [4, 5]
    assert mean == 3
    assert std_dev == 1

    # Test case 4: With threshold
    data = np.array([1, 2, 3, 4, 5, 100])
    outliers, mean, std_dev = task_func(data, threshold=3)
    assert outliers == [4]
    assert mean == 3
    assert std_dev == 1

    # Test case 5: With threshold and multiple outliers
    data = np.array([1, 2, 3, 4, 5, 100, 200])
    outliers, mean, std_dev = task_func(data, threshold=3)
    assert outliers == [4, 5]
    assert mean == 3
    assert std_dev == 1