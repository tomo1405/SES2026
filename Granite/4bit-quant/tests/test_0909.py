import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import pytest

from src_0909 import task_func

@pytest.fixture
def setup():
    directory = 'path/to/directory'
    pattern = r'pattern'
    return directory, pattern

def test_task_func(setup):
    directory, pattern = setup
    plots = task_func(directory, pattern)
    assert isinstance(plots, list)
    for ax in plots:
        assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_directory(setup):
    directory, pattern = setup
    with pytest.raises(FileNotFoundError):
        task_func('invalid_directory', pattern)

def test_task_func_with_invalid_pattern(setup):
    directory, pattern = setup
    with pytest.raises(ValueError):
        task_func(directory, 'invalid_pattern')