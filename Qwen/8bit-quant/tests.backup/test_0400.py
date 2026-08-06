import pytest
from src_0400 import task_func

def test_task_func_valid_input():
    frequency = 1
    sample_size = 10000
    fig, ax = task_func(frequency, sample_size)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == 2
    assert ax.lines[0].get_label() == 'sin'
    assert ax.lines[1].get_label() == 'cos'

def test_task_func_negative_frequency():
    with pytest.raises(ValueError, match="Frequency cannot be negative"):
        task_func(-1)

def test_task_func_zero_sample_size():
    with pytest.raises(ValueError, match="Sample size cannot be negative or zero"):
        task_func(1, 0)

def test_task_func_negative_sample_size():
    with pytest.raises(ValueError, match="Sample size cannot be negative or zero"):
        task_func(1, -1)