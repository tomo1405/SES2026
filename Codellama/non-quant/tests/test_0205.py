import pytest
from src_0205 import task_func
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def test_task_func():
    L = [1, 2, 3, 4, 5]
    result = task_func(L)
    assert result['mean'] == np.mean(L)
    assert result['median'] == np.median(L)
    assert result['mode'] == Counter(L).most_common(1)[0][0]
    assert result['std_dev'] == np.std(L)
    assert isinstance(result['plot'], plt.gca)