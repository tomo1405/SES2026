import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_0661 import task_func


@pytest.fixture
def sample_data():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    labels = ['Dataset 1', 'Dataset 2']
    return x, y, labels

def test_task_func_returns_figure(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_plots_correct_number_of_datasets(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    ax = fig.axes[0]
    assert len(ax.lines) == len(x)

def test_task_func_scales_data_correctly(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    ax = fig.axes[0]

    for i, line in enumerate(ax.lines):
        xy = np.vstack((x[i], y[i])).T
        scaler = StandardScaler()
        xy_scaled = scaler.fit_transform(xy)
        assert np.allclose(line.get_xdata(), xy_scaled[:, 0])
        assert np.allclose(line.get_ydata(), xy_scaled[:, 1])

def test_task_func_adds_legend(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    ax = fig.axes[0]
    assert ax.get_legend() is not None
    assert [text.get_text() for text in ax.get_legend().get_texts()] == labels

def test_task_func_handles_empty_input():
    x = []
    y = []
    labels = []
    fig = task_func(x, y, labels)
    ax = fig.axes[0]
    assert len(ax.lines) == 0
    assert ax.get_legend() is None