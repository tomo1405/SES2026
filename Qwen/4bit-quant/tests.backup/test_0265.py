import pytest
from src_0265 import task_func
import numpy as np
import pandas as pd

def test_task_func_updates_dictionary():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    updated_dict, _, _ = task_func(dictionary, key, value)
    assert updated_dict == {'a': 1, 'b': 2}

def test_task_func_value_must_be_number():
    with pytest.raises(ValueError, match="Value must be a number."):
        task_func({}, 'key', 'not_a_number')

def test_task_func_data_type():
    _, data, _ = task_func({}, 'key', 10)
    assert isinstance(data, pd.Series)

def test_task_func_data_length():
    n = 100
    _, data, _ = task_func({}, 'key', 10, n=n)
    assert len(data) == n

def test_task_func_data_distribution():
    np.random.seed(0)
    _, data, _ = task_func({}, 'key', 10, n=1000)
    mean = np.mean(data)
    std = np.std(data)
    assert np.isclose(mean, 10, atol=1e-2)
    assert np.isclose(std, 10, atol=1e-2)

def test_task_func_plot_axis():
    _, _, ax = task_func({}, 'key', 10)
    assert isinstance(ax, plt.Axes)