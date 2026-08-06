python
import pytest
from src_1072 import task_func

def test_task_func():
    list_of_lists = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    fig, ax = task_func(list_of_lists)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert len(ax.lines) == len(list_of_lists)
    assert all(isinstance(line, plt.Line2D) for line in ax.lines)
    assert all(line.get_color() in COLORS for line in ax.lines)
    assert all(line.get_data()[0].shape == (3,) for line in ax.lines)
    assert all(line.get_data()[1].shape == (3,) for line in ax.lines)
    assert all(line.get_data()[0].dtype == np.int64 for line in ax.lines)
    assert all(line.get_data()[1].dtype == np.int64 for line in ax.lines)
    assert all(line.get_data()[0].min() == 1 for line in ax.lines)
    assert all(line.get_data()[0].max() == 3 for line in ax.lines)
    assert all(line.get_data()[1].min() == 1 for line in ax.lines)
    assert all(line.get_data()[1].max() == 3 for line in ax.lines)
    assert all(line.get_data()[0].tolist() == [1, 2, 3] for line in ax.lines)
    assert all(line.get_data()[1].tolist() == [1, 2, 3] for line in ax.lines)