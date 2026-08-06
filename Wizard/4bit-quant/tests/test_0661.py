python
import pytest
from src_0661 import task_func

def test_task_func():
    # Test case 1: Test with 2 datasets
    x = [np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])]
    y = [np.array([[10, 20], [30, 40]]), np.array([[50, 60], [70, 80]])]
    labels = ['Dataset 1', 'Dataset 2']

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)  # Check if the returned object is a matplotlib Figure object
    assert len(fig.axes) == 1  # Check if there is only one axis in the figure
    assert len(fig.axes[0].lines) == 2  # Check if there are two lines in the axis
    assert fig.axes[0].lines[0].get_label() == 'Dataset 1'  # Check if the first line has the correct label
    assert fig.axes[0].lines[1].get_label() == 'Dataset 2'  # Check if the second line has the correct label

    # Test case 2: Test with 1 dataset
    x = [np.array([[1, 2], [3, 4]])]
    y = [np.array([[10, 20], [30, 40]])]
    labels = ['Dataset 1']

    fig = task_func(x, y, labels)

    assert isinstance(fig, plt.Figure)  # Check if the returned object is a matplotlib Figure object
    assert len(fig.axes) == 1  # Check if there is only one axis in the figure
    assert len(fig.axes[0].lines) == 1  # Check if there is only one line in the axis
    assert fig.axes[0].lines[0].get_label() == 'Dataset 1'  # Check if the line has the correct label