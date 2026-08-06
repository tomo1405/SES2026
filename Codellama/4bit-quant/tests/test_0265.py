import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from src_0265 import task_func


def test_task_func():
    # Test that the function raises an error when value is not a number
    with pytest.raises(ValueError):
        task_func({}, "key", "value")

    # Test that the function updates the dictionary correctly
    dictionary = {}
    key = "key"
    value = 10
    n = 100
    bins = 30
    seed = 0
    np.random.seed(seed)
    data = np.random.normal(loc=float(value), scale=float(value), size=n)
    _, ax = plt.subplots()
    ax.hist(data, bins=bins, density=True)
    data = pd.Series(data)
    dictionary, data, ax = task_func(dictionary, key, value, n, bins, seed)
    assert dictionary[key] == value

    # Test that the function returns the correct data and axes object
    assert data.equals(np.random.normal(loc=float(value), scale=float(value), size=n))
    assert ax.get_xlabel() == "Value"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Histogram of Generated Data"