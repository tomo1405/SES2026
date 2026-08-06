import pytest
from src_0213 import task_func

def test_task_func():
    data = [(1, 2), (3, 4), (5, 6)]
    ax, max_y_point = task_func(data)
    assert ax is not None
    assert max_y_point in data
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Points with Max Y Point Highlighted'
    assert ax.legend().get_texts()[0].get_text() == 'Points'
    assert ax.legend().get_texts()[1].get_text() == 'Max Y Point'