import pytest
from src_0661 import task_func
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    labels = ['Dataset 1', 'Dataset 2']
    return x, y, labels

def test_task_func(sample_data):
    x, y, labels = sample_data
    fig = task_func(x, y, labels)
    
    # Check if the returned object is a matplotlib Figure
    assert isinstance(fig, plt.Figure), "The returned object should be a matplotlib Figure"
    
    # Check if the plot has the correct number of lines (datasets)
    ax = fig.axes[0]
    assert len(ax.get_lines()) == len(x), "The number of plotted lines should match the number of datasets"

    # Check if the legend has the correct labels
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels, "The legend labels should match the provided labels"

    # Close the plot to free up resources
    plt.close(fig)

def test_task_func_with_empty_data():
    x = [np.array([]), np.array([])]
    y = [np.array([]), np.array([])]
    labels = ['Dataset 1', 'Dataset 2']
    fig = task_func(x, y, labels)
    
    # Check if the returned object is a matplotlib Figure
    assert isinstance(fig, plt.Figure), "The returned object should be a matplotlib Figure"
    
    # Check if the plot has no lines
    ax = fig.axes[0]
    assert len(ax.get_lines()) == 0, "The plot should have no lines when the input data is empty"

    # Close the plot to free up resources
    plt.close(fig)

def test_task_func_with_single_dataset():
    x = [np.array([1, 2, 3])]
    y = [np.array([4, 5, 6])]
    labels = ['Dataset 1']
    fig = task_func(x, y, labels)
    
    # Check if the returned object is a matplotlib Figure
    assert isinstance(fig, plt.Figure), "The returned object should be a matplotlib Figure"
    
    # Check if the plot has one line
    ax = fig.axes[0]
    assert len(ax.get_lines()) == 1, "The plot should have one line when there is a single dataset"

    # Check if the legend has the correct label
    legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
    assert legend_labels == labels, "The legend label should match the provided label"

    # Close the plot to free up resources
    plt.close(fig)