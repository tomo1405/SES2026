python
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pytest

from src_0996 import task_func

def test_task_func():
    # Test if file exists
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.csv", "plot.png")

    # Test empty file
    with pytest.raises(pd.errors.EmptyDataError):
        task_func("empty_file.csv", "plot.png")

    # Test non-numeric data
    data = pd.DataFrame({"A": ["a", "b", "c"], "B": [1, 2, 3]})
    mean, median, plot_path = task_func(data, "plot.png")
    assert np.isnan(mean)
    assert np.isnan(median)
    assert os.path.isfile(plot_path)

    # Test numeric data
    data = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]})
    mean, median, plot_path = task_func(data, "plot.png")
    assert mean == 3.0
    assert median == 3.0
    assert os.path.isfile(plot_path)

    # Test empty data
    data = pd.DataFrame({"A": [], "B": []})
    mean, median, plot_path = task_func(data, "plot.png")
    assert np.isnan(mean)
    assert np.isnan(median)
    assert os.path.isfile(plot_path)