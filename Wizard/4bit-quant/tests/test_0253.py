python
import pytest
from src_0253 import task_func

def test_task_func():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    labels = ['A', 'B', 'C']
    ax = task_func(data, labels)
    assert ax.get_xlabel() == 'Index'
    assert ax.get_ylabel() == 'Value'
    assert ax.get_title() == 'Task Function'
    assert ax.get_legend_handles_labels()[1] == labels
    assert ax.get_legend_handles_labels()[0][0].get_color() == COLORS[0]
    assert ax.get_legend_handles_labels()[0][1].get_color() == COLORS[1]
    assert ax.get_legend_handles_labels()[0][2].get_color() == COLORS[2]
    assert ax.get_legend_handles_labels()[0][3].get_color() == COLORS[3]
    assert ax.get_legend_handles_labels()[0][4].get_color() == COLORS[4]
    assert ax.get_lines()[0].get_data()[0] == data[0]
    assert ax.get_lines()[1].get_data()[0] == data[1]
    assert ax.get_lines()[2].get_data()[0] == data[2]
    assert ax.get_lines()[0].get_label() == labels[0]
    assert ax.get_lines()[1].get_label() == labels[1]
    assert ax.get_lines()[2].get_label() == labels[2]
    assert ax.get_lines()[0].get_color() == COLORS[0]
    assert ax.get_lines()[1].get_color() == COLORS[1]
    assert ax.get_lines()[2].get_color() == COLORS[2]
    assert ax.get_lines()[3].get_color() == COLORS[3]
    assert ax.get_lines()[4].get_color() == COLORS[4]