import pytest
from src_0125 import task_func
import matplotlib.pyplot as plt

def test_task_func_input_type():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_input_elements():
    with pytest.raises(ValueError):
        task_func([1, "two", 3])

def test_task_func_output_type():
    execution_time, ax = task_func([1, 2, 3])
    assert isinstance(execution_time, float)
    assert isinstance(ax, plt.Axes)

def test_task_func_execution_time():
    execution_time, _ = task_func([1, 2, 3], size=10)
    assert execution_time > 0

def test_task_func_histogram():
    _, ax = task_func([1, 2, 3], size=10)
    assert len(ax.patches) == 20  # 20 bins

def test_task_func_random_list_length():
    execution_time, ax = task_func([1, 2, 3], size=5)
    random_list = [patch.get_height() for patch in ax.patches]
    assert sum(random_list) == 5  # Total number of elements should match the size parameter

def test_task_func_seed_consistency():
    _, ax1 = task_func([1, 2, 3], size=10, seed=42)
    _, ax2 = task_func([1, 2, 3], size=10, seed=42)
    heights1 = [patch.get_height() for patch in ax1.patches]
    heights2 = [patch.get_height() for patch in ax2.patches]
    assert heights1 == heights2  # Histograms should be identical with the same seed