import pytest
from src_0525 import task_func
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

@pytest.fixture
def sample_data():
    return [
        {"a": 1, "b": 2},
        {"a": 2, "b": 3},
        {"a": 3, "b": 4}
    ]

def test_task_func_valid_input(sample_data):
    result, _ = task_func(sample_data)
    assert isinstance(result, dict), "The result should be a dictionary."
    assert all(isinstance(value, dict) for value in result.values()), "Each value in the result should be a dictionary."
    assert all(isinstance(mean, (int, float)) and isinstance(std, (int, float)) for mean, std in result.values()), "Each mean and std should be a number."

def test_task_func_invalid_input(sample_data):
    with pytest.raises(ValueError):
        task_func([])
    invalid_data = ["not a list", "not a list either"]
    with pytest.raises(TypeError):
        task_func(invalid_data)
    invalid_data = [{"a": "not a number"}, {"b": 2}]
    with pytest.raises(TypeError):
        task_func(invalid_data)

def test_visualization(sample_data):
    result, axes = task_func(sample_data)
    assert len(axes) == len(result), "The number of plots should match the number of statistics."
    for ax in axes:
        assert isinstance(ax, plt.Axes), "Each axis should be a matplotlib axis."