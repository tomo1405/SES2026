import pytest
from src_0197 import task_func
import numpy as np

def test_task_func_length():
    axes, numbers = task_func(10)
    assert len(numbers) == 10

def test_task_func_range_limit():
    axes, numbers = task_func(10, range_limit=50)
    assert all(1 <= num <= 50 for num in numbers)

def test_task_func_seed():
    axes1, numbers1 = task_func(10, seed=42)
    axes2, numbers2 = task_func(10, seed=42)
    assert numbers1 == numbers2

def test_task_func_invalid_range_limit():
    with pytest.raises(ValueError):
        task_func(10, range_limit=1)

def test_task_func_sorted_numbers():
    axes, numbers = task_func(10)
    assert numbers == sorted(numbers)

def test_task_func_axes_not_none():
    axes, numbers = task_func(10)
    assert axes is not None

def test_task_func_random_numbers_distribution():
    _, numbers = task_func(1000, range_limit=100, seed=0)
    counts = np.bincount(numbers, minlength=101)[1:]  # Exclude 0 index
    assert np.all(counts > 0)  # Ensure all numbers appear at least once