import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src_1080 import task_func

def test_task_func():
    data = [["100", "200", "300"], ["400", "500", "600"]]
    expected_mean = 350
    expected_median = 350
    expected_std_dev = 173.20508075688772

    result, ax = task_func(data)

    assert result["mean"] == expected_mean
    assert result["median"] == expected_median
    assert result["std_dev"] == expected_std_dev
    assert isinstance(ax, tuple)
    assert len(ax) == 2
    assert isinstance(ax[0], np.ndarray)
    assert isinstance(ax[1], plt.Axes)