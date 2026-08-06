import pytest
from src_0400 import task_func

def test_task_func_positive_frequency():
    frequency = 10
    sample_size = 10000
    fig, ax = task_func(frequency, sample_size)
    assert fig is not None
    assert ax is not None
    assert len(ax.lines) == 2
    assert ax.lines[0].get_label() == 'sin'
    assert ax.lines[1].get_label() == 'cos'

def test_task_func_negative_frequency():
    frequency = -10
    sample_size = 10000
    with pytest.raises(ValueError):
        task_func(frequency, sample_size)

def test_task_func_negative_sample_size():
    frequency = 10
    sample_size = -10000
    with pytest.raises(ValueError):
        task_func(frequency, sample_size)

def test_task_func_zero_sample_size():
    frequency = 10
    sample_size = 0
    with pytest.raises(ValueError):
        task_func(frequency, sample_size)