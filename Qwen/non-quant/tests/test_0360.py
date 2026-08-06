import pytest
from src_0360 import task_func
from scipy import stats
import matplotlib.pyplot as plt
import io
import numpy as np

@pytest.fixture
def sample_data():
    return {
        'x': np.array([1, 2, 3, 4, 5]),
        'y': np.array([2, 4, 6, 8, 10])
    }

def test_task_func_correlation(sample_data):
    data_keys = ['x', 'y']
    correlation, ax = task_func(sample_data, data_keys)
    expected_correlation, _ = stats.pearsonr(sample_data['x'], sample_data['y'])
    assert np.isclose(correlation, expected_correlation)

def test_task_func_plot(sample_data):
    data_keys = ['x', 'y']
    _, ax = task_func(sample_data, data_keys)
    assert isinstance(ax, plt.Axes)
    # Capture the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Check if the buffer is not empty
    assert buf.getbuffer().nbytes > 0