import pytest
from src_0211 import task_func

def test_task_func():
    data = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    result = task_func(data)

    assert result.get_xlabel() == 'Letter'
    assert result.get_ylabel() == 'Count'
    assert result.get_title() == 'Letter Counts with Max Value Letter Highlighted'
    assert result.get_legend() == 'Letter Counts'

    assert len(result.get_xticks()) == 5
    assert len(result.get_yticks()) == 5

    assert result.get_xticklabels() == ['a', 'b', 'c', 'd', 'e']
    assert result.get_yticklabels() == ['1', '2', '3', '4', '5']

    assert result.get_bar_labels() == ['a', 'b', 'c', 'd', 'e']
    assert result.get_bar_heights() == [1, 2, 3, 4, 5]

    assert result.get_bar_colors() == ['red']
    assert result.get_bar_labels() == ['Max Value Letter']