import pytest
from src_1002 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    ax = task_func(csv_file_path)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_title() == "Plot Title : Normalized Column 1"
    assert ax.get_xlabel() == "Index : Normalized Value"
    assert ax.get_ylabel() == "Frequency : Normalized Value"
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_xticks() == [0, 0.2, 0.4, 0.6, 0.8, 1]
    assert ax.get_yticks() == [0, 0.2, 0.4, 0.6, 0.8, 1]
    assert ax.get_xticklabels() == ["0", "0.2", "0.4", "0.6", "0.8", "1"]
    assert ax.get_yticklabels() == ["0", "0.2", "0.4", "0.6", "0.8", "1"]