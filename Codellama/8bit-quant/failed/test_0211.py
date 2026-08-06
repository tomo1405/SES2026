import pytest
from src_0211 import task_func

def test_task_func():
    data = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    result = task_func(data)

    assert isinstance(result, matplotlib.axes.Axes)
    assert result.get_xlabel() == 'Letter'
    assert result.get_ylabel() == 'Count'
    assert result.get_title() == 'Letter Counts with Max Value Letter Highlighted'
    assert len(result.get_legend_handles_labels()[0]) == 2
    assert len(result.get_legend_handles_labels()[1]) == 2
    assert result.get_legend_handles_labels()[0][0].get_label() == 'Letter Counts'
    assert result.get_legend_handles_labels()[0][1].get_label() == 'Max Value Letter'
    assert result.get_legend_handles_labels()[1][0].get_label() == 'Letter Counts'
    assert result.get_legend_handles_labels()[1][1].get_label() == 'Max Value Letter'