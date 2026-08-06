import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0358 import task_func


# Mocking plt.show to prevent actual plotting during tests
class MockPlot:
    def plot(self, *args, **kwargs):
        pass

    def legend(self):
        pass

    def grid(self):
        pass

    def show(self):
        pass

@pytest.fixture
def mock_plot(monkeypatch):
    monkeypatch.setattr(plt, 'plot', MockPlot().plot)
    monkeypatch.setattr(plt, 'legend', MockPlot().legend)
    monkeypatch.setattr(plt, 'grid', MockPlot().grid)
    monkeypatch.setattr(plt, 'show', MockPlot().show)

def test_task_func_type_check(mock_plot):
    with pytest.raises(TypeError, match="x must be numpy.ndarray"):
        task_func([1, 2, 3])

def test_task_func_output(mock_plot):
    x = np.array([-3, -2, -1, 0, 1, 2, 3])
    result = task_func(x)
    assert isinstance(result, np.ndarray)
    assert result.dtype == np.complex128
    assert result.shape == x.shape

def test_task_func_real_part_values(mock_plot):
    x = np.array([0])
    result = task_func(x)
    expected_real = norm.pdf(0, 0, 1)
    assert np.isclose(result.real, expected_real)

def test_task_func_imaginary_part_values(mock_plot):
    x = np.array([0])
    result = task_func(x)
    expected_imag = norm.pdf(0, 2, 2)
    assert np.isclose(result.imag, expected_imag)