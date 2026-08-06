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
    dictionary, data, ax = task_func(dictionary, key, value)
    assert dictionary[key] == value

    # Test that the function generates the correct histogram
    n = 100
    bins = 30
    seed = 0
    np.random.seed(seed)
    data = np.random.normal(loc=float(value), scale=float(value), size=n)
    _, ax = plt.subplots()
    ax.hist(data, bins=bins, density=True)
    data = pd.Series(data)
    assert np.allclose(data.hist(bins=bins, density=True), ax.hist(bins=bins, density=True))