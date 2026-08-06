import pytest
from src_0905 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: Test with a list of dictionaries
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    keys = ['x', 'y', 'z']
    ax = task_func(d, keys)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_legend() is not None

    # Test case 2: Test with a list of dictionaries and a single key
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    keys = ['x']
    ax = task_func(d, keys)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_legend() is None

    # Test case 3: Test with a list of dictionaries and a non-existent key
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    keys = ['a']
    ax = task_func(d, keys)
    assert isinstance(ax, plt.Axes)
    assert not ax.has_data()
    assert ax.get_legend() is None

    # Test case 4: Test with a list of dictionaries and a list of keys
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    keys = ['x', 'y']
    ax = task_func(d, keys)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_legend() is not None

    # Test case 5: Test with a list of dictionaries and a list of keys with a non-existent key
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    keys = ['x', 'a']
    ax = task_func(d, keys)
    assert isinstance(ax, plt.Axes)
    assert ax.has_data()
    assert ax.get_legend() is not None

    # Test case 6: Test with a list of dictionaries and a list of keys with a non-existent key
    d = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}]
    keys = ['a', 'b']
    ax = task_func(d, keys)
    assert isinstance(ax, plt.Axes)
    assert not ax.has_data()
    assert ax.get_legend() is None