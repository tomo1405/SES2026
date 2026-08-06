import pytest
from src_0265 import task_func
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

@pytest.fixture
def setup():
    dictionary = {}
    key = "test_key"
    value = 5
    n = 100
    bins = 30
    seed = 0
    return dictionary, key, value, n, bins, seed

def test_task_func(setup):
    dictionary, key, value, n, bins, seed = setup
    result = task_func(dictionary, key, value, n, bins, seed)
    
    assert isinstance(result, tuple), "The function should return a tuple"
    assert len(result) == 3, "The function should return a tuple with three elements"
    
    dictionary, data, ax = result
    assert isinstance(dictionary, dict), "The first element should be a dictionary"
    assert isinstance(data, pd.Series), "The second element should be a pandas Series"
    assert isinstance(ax, plt.Axes), "The third element should be a matplotlib Axes object"
    
    # Additional assertions to check the functionality
    assert key in dictionary, "The dictionary should be updated with the new key-value pair"
    assert np.isclose(np.mean(data), value, rtol=1e-1), "The data generated should have the specified mean"

    plt.close()  # Close the plot to avoid memory leaks