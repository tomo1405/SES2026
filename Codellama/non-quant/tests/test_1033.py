import matplotlib
from src_1033 import task_func


def test_task_func():
    # Test with default parameters
    ax = task_func()
    assert ax is not None
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Heatmap"
    assert ax.get_xlabel() == "Letter"
    assert ax.get_ylabel() == "Letter"
    assert ax.get_xticklabels() == LETTERS
    assert ax.get_yticklabels() == LETTERS
    assert ax.get_xticks() == range(len(LETTERS))
    assert ax.get_yticks() == range(len(LETTERS))
    assert ax.get_data() == corr.values

    # Test with custom parameters
    ax = task_func(rows=500, string_length=5)
    assert ax is not None
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Heatmap"
    assert ax.get_xlabel() == "Letter"
    assert ax.get_ylabel() == "Letter"
    assert ax.get_xticklabels() == LETTERS
    assert ax.get_yticklabels() == LETTERS
    assert ax.get_xticks() == range(len(LETTERS))
    assert ax.get_yticks() == range(len(LETTERS))
    assert ax.get_data() == corr.values

    # Test with empty DataFrame
    ax = task_func(rows=0, string_length=3)
    assert ax is None