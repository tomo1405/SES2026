import pytest
from src_0660 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    x = [np.linspace(-3, 3, 100), np.linspace(-2, 2, 100)]
    y = [np.random.normal(0, 1, 100), np.random.normal(1, 0.5, 100)]
    labels = ['Normal(0, 1)', 'Normal(1, 0.5)']
    return x, y, labels

def test_task_func_returns_figure(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    assert isinstance(fig, plt.Figure)

def test_task_func_plots_correct_number_of_lines(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    ax = fig.axes[0]
    assert len(ax.lines) == len(labels)

def test_task_func_legends_correctly(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    ax = fig.axes[0]
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels

def test_task_func_plots_correct_pdf(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    ax = fig.axes[0]
    
    for i, line in enumerate(ax.lines):
        mu = np.mean(y[i])
        sigma = np.std(y[i])
        expected_pdf = stats.norm.pdf(x[i], mu, sigma)
        assert np.allclose(line.get_ydata(), expected_pdf)