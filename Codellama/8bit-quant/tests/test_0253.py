import pytest
from src_0253 import task_func

def test_task_func():
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    labels = ['Series 1', 'Series 2', 'Series 3']
    ax = task_func(data, labels)
    assert ax.get_legend().get_texts()[0].get_text() == 'Series 1'
    assert ax.get_legend().get_texts()[1].get_text() == 'Series 2'
    assert ax.get_legend().get_texts()[2].get_text() == 'Series 3'
    assert ax.get_legend().get_texts()[0].get_color() == 'red'
    assert ax.get_legend().get_texts()[1].get_color() == 'green'
    assert ax.get_legend().get_texts()[2].get_color() == 'blue'