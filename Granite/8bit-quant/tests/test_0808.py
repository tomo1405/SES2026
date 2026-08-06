import numpy as np
from scipy.stats import norm
from src_0808 import task_func

def test_task_func():
    data = np.array([1, 2, 3, 4, 5])
    threshold = 2.0
    outliers, mean, var = task_func(data, threshold)
    assert isinstance(outliers, list)
    assert isinstance(mean, float)
    assert isinstance(var, float)
    assert len(outliers) == 0
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 100])
    threshold = 2.0
    outliers, mean, var = task_func(data, threshold)
    assert isinstance(outliers, list)
    assert isinstance(mean, float)
    assert isinstance(var, float)
    assert len(outliers) == 1
    assert outliers[0] == 9