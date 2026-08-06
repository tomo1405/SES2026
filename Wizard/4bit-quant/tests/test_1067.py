python
import numpy as np
import matplotlib.pyplot as plt
from src_1067 import task_func

def test_task_func():
    # Test with default values
    data, outliers_detected, ax = task_func()
    assert len(data) == 105
    assert len(outliers_detected) == 5
    assert ax is not None

    # Test with custom values
    data, outliers_detected, ax = task_func(num_samples=10, num_outliers=3)
    assert len(data) == 13
    assert len(outliers_detected) == 3
    assert ax is not None

    # Test with no normal data
    data, outliers_detected, ax = task_func(num_samples=0, num_outliers=5)
    assert len(data) == 5
    assert len(outliers_detected) == 5
    assert ax is not None