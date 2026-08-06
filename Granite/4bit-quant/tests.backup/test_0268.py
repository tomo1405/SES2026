import pytest
from src_0268 import task_func

def test_task_func():
    data = {'a': 1, 'b': 2, 'c': 3}
    fft, ax = task_func(data)
    assert isinstance(fft, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_sample_rate():
    data = {'a': 1, 'b': 2, 'c': 3}
    fft, ax = task_func(data, sample_rate=44100)
    assert isinstance(fft, np.ndarray)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_invalid_sample_rate():
    data = {'a': 1, 'b': 2, 'c': 3}
    with pytest.raises(ValueError):
        fft, ax = task_func(data, sample_rate=-1)