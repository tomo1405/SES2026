import pytest
from src_0575 import task_func

def test_task_func():
    ax = task_func()
    assert ax is not None
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'

def test_task_func_with_noise():
    ax = task_func(noise_level=0.5)
    assert ax is not None
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'

def test_task_func_with_long_array():
    ax = task_func(array_length=200)
    assert ax is not None
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'

def test_task_func_with_all_params():
    ax = task_func(array_length=200, noise_level=0.5)
    assert ax is not None
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'