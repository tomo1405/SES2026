import pytest
from src_0265 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_updates_dictionary():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    updated_dict, _, _ = task_func(dictionary, key, value)
    assert updated_dict == {'a': 1, 'b': 2}

def test_task_func_value_must_be_number():
    dictionary = {'a': 1}
    key = 'b'
    value = 'not_a_number'
    with pytest.raises(ValueError, match="Value must be a number."):
        task_func(dictionary, key, value)

def test_task_func_generates_correct_data_shape():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    _, data, _ = task_func(dictionary, key, value, n=50)
    assert len(data) == 50

def test_task_func_generates_correct_data_distribution():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    _, data, _ = task_func(dictionary, key, value, n=1000, seed=42)
    mean = np.mean(data)
    std = np.std(data)
    assert np.isclose(mean, value, atol=0.1)
    assert np.isclose(std, value, atol=0.1)

def test_task_func_returns_correct_axes_object():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    _, _, ax = task_func(dictionary, key, value)
    assert isinstance(ax, plt.Axes)

def test_task_func_bins_parameter():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    _, _, ax = task_func(dictionary, key, value, bins=10)
    assert len(ax.patches) == 10

def test_task_func_seed_parameter():
    dictionary = {'a': 1}
    key = 'b'
    value = 2
    _, data1, _ = task_func(dictionary, key, value, seed=42)
    _, data2, _ = task_func(dictionary, key, value, seed=42)
    assert np.array_equal(data1, data2)