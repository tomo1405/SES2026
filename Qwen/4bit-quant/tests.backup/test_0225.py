import pytest
from src_0225 import task_func
import numpy as np

def test_task_func_range_validation():
    with pytest.raises(ValueError):
        task_func(range_start=10, range_end=-10)

def test_task_func_return_types():
    data, ax, mean_fft, median_fft = task_func()
    assert isinstance(data, tuple)
    assert isinstance(ax, plt.Axes)
    assert isinstance(mean_fft, float)
    assert isinstance(median_fft, float)

def test_task_func_data_generator():
    data, _, _, _ = task_func()
    for x, sin_x, cos_x, abs_x in data:
        assert isinstance(x, float)
        assert isinstance(sin_x, float)
        assert isinstance(cos_x, float)
        assert isinstance(abs_x, float)

def test_task_func_fft_values():
    _, _, mean_fft, median_fft = task_func()
    assert mean_fft >= 0
    assert median_fft >= 0

def test_task_func_plot():
    _, ax, _, _ = task_func()
    assert len(ax.collections) == 3 * 201  # 201 points with 3 scatter plots each

def test_task_func_with_custom_parameters():
    data, ax, mean_fft, median_fft = task_func(range_start=0, range_end=np.pi, step=np.pi/10)
    for x, sin_x, cos_x, abs_x in data:
        assert x >= 0 and x <= np.pi
    assert mean_fft >= 0
    assert median_fft >= 0