import pytest
from src_0265 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_updates_dictionary():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    result_dict, _, _ = task_func(dictionary, key, value)
    assert result_dict == {'a': 1, 'b': 2}

def test_task_func_value_must_be_number():
    dictionary = {'a': 1}
    key = 'b'
    value = 'not_a_number'
    with pytest.raises(ValueError, match="Value must be a number."):
        task_func(dictionary, key, value)

def test_task_func_generates_correct_data_size():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    n = 100
    _, data, _ = task_func(dictionary, key, value, n=n)
    assert len(data) == n

def test_task_func_data_is_series():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    _, data, _ = task_func(dictionary, key, value)
    assert isinstance(data, pd.Series)

def test_task_func_plot_returns_axes():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    _, _, ax = task_func(dictionary, key, value)
    assert isinstance(ax, plt.Axes)

def test_task_func_random_seed():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    seed = 0
    _, data1, _ = task_func(dictionary, key, value, seed=seed)
    _, data2, _ = task_func(dictionary, key, value, seed=seed)
    assert np.array_equal(data1, data2)