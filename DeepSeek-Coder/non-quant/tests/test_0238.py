import pytest
from src_0238 import task_func
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

@pytest.fixture
def sample_data():
    data = [
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6),
        ('item3', 7, 8, 9)
    ]
    return data

def test_task_func(sample_data):
    data = sample_data
    result = task_func(data)
    assert isinstance(result, np.ndarray)
    assert result.shape == (len(data), 2)

def test_plot_save(tmp_path):
    data = [
        ('item1', 1, 2, 3),
        ('item2', 4, 5, 6),
        ('item3', 7, 8, 9)
    ]
    plot_path = tmp_path / "test_plot.png"
    result = task_func(data, save_plot=True, plot_path=plot_path)
    assert plot_path.exists()