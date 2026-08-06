import pytest
from src_0211 import task_func

def test_task_func():
    data = [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]
    ax = task_func(data)
    assert ax is not None
    assert ax.get_xlabel() == "Letter"
    assert ax.get_ylabel() == "Count"
    assert ax.get_title() == "Letter Counts with Max Value Letter Highlighted"
    assert ax.patches[0].get_height() == 5
    assert ax.patches[0].get_xy() == (0.5, 0.0)
    assert ax.patches[1].get_height() == 4
    assert ax.patches[1].get_xy() == (1.5, 1.0)
    assert ax.patches[2].get_height() == 3
    assert ax.patches[2].get_xy() == (2.5, 2.0)
    assert ax.patches[3].get_height() == 2
    assert ax.patches[3].get_xy() == (3.5, 3.0)
    assert ax.patches[4].get_height() == 1
    assert ax.patches[4].get_xy() == (4.5, 4.0)