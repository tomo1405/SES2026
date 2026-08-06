import pytest
from src_0125 import task_func
import matplotlib.pyplot as plt

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_non_numeric_elements():
    with pytest.raises(ValueError):
        task_func([1, "two", 3])

def test_task_func_with_default_values():
    result = task_func([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], plt.Axes)

def test_task_func_with_custom_size():
    result = task_func([1, 2, 3], size=50)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], plt.Axes)

def test_task_func_with_custom_seed():
    result = task_func([1, 2, 3], seed=42)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], plt.Axes)

def test_task_func_with_large_sum():
    result = task_func([100, 200, 300])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], plt.Axes)

def test_task_func_with_small_sum():
    result = task_func([1, 2, 3])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], float)
    assert isinstance(result[1], plt.Axes)