import pytest
from src_1080 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    data = [
        {"Price_String": "100", "Price_Float": 100.0},
        {"Price_String": "200", "Price_Float": 200.0},
        {"Price_String": "300", "Price_Float": 300.0},
        {"Price_String": "400", "Price_Float": 400.0},
        {"Price_String": "500", "Price_Float": 500.0},
    ]
    expected_mean = 300.0
    expected_median = 300.0
    expected_std_dev = 100.0

    result, ax = task_func(data)

    assert result["mean"] == expected_mean
    assert result["median"] == expected_median
    assert result["std_dev"] == expected_std_dev

    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Histogram of Product Prices"
    assert ax.get_xlabel() == "Price"
    assert ax.get_ylabel() == "Frequency"