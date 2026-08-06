import pytest
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from src_0525 import task_func

def test_task_func_with_empty_data():
    with pytest.raises(ValueError) as excinfo:
        task_func([])
    assert "Input data is empty." in str(excinfo.value)

def test_task_func_with_invalid_data_type():
    with pytest.raises(TypeError) as excinfo:
        task_func("invalid data")
    assert "Input must be a list of dictionaries." in str(excinfo.value)

def test_task_func_with_invalid_dictionary_values():
    with pytest.raises(TypeError) as excinfo:
        task_func([{"key": "value"}])
    assert "All values in the dictionaries must be numeric." in str(excinfo.value)

def test_task_func_with_valid_data():
    data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    result, axes = task_func(data)
    assert isinstance(result, dict)
    assert all(isinstance(value, dict) for value in result.values())
    assert all(key in result for key in ["a", "b"])
    assert all(isinstance(value["mean"], float) for value in result.values())
    assert all(isinstance(value["std"], float) for value in result.values())
    assert isinstance(axes, list)
    assert all(isinstance(ax, plt.Axes) for ax in axes)