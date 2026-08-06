import pytest
from src_0210 import task_func

def test_task_func():
    data = [(1, 2), (3, 4), (5, 6)]
    ax = task_func(data)
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    assert ax.get_title() == 'Max Tuple Highlighted'
    assert ax.legend().get_texts()[0].get_text() == 'Data'
    assert ax.legend().get_texts()[1].get_text() == 'Max Tuple'