import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0358 import task_func


@pytest.fixture
def sample_x():
    return np.array([-3, -2, -1, 0, 1, 2, 3])

def test_task_func_type_check(sample_x):
    with pytest.raises(TypeError):
        task_func([1, 2, 3])  # Passing a list instead of a numpy array

def test_task_func_output(sample_x):
    result = task_func(sample_x)
    assert isinstance(result, np.ndarray), "The result should be a numpy array"
    assert result.shape == sample_x.shape, "The result shape should match the input shape"
    assert np.iscomplexobj(result), "The result should be a complex numpy array"

def test_task_func_plotting(sample_x, monkeypatch):
    # Mocking the plot function to prevent actual plotting
    monkeypatch.setattr(plt, 'plot', lambda *args, **kwargs: None)
    monkeypatch.setattr(plt, 'legend', lambda: None)
    monkeypatch.setattr(plt, 'grid', lambda: None)
    monkeypatch.setattr(plt, 'show', lambda: None)

    task_func(sample_x)  # This should not raise any exceptions due to plotting

def test_task_func_real_imag_parts(sample_x):
    result = task_func(sample_x)
    real_part = norm.pdf(sample_x, 0, 1)
    imag_part = norm.pdf(sample_x, 2, 2)
    expected_complex_dist = real_part + 1j * imag_part

    np.testing.assert_array_almost_equal(result.real, expected_complex_dist.real)
    np.testing.assert_array_almost_equal(result.imag, expected_complex_dist.imag)