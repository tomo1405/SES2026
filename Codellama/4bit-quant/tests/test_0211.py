import pytest
from src_0211 import task_func

def test_task_func():
    data = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
    expected_letters = ['a', 'b', 'c', 'd', 'e']
    expected_counts = [1, 2, 3, 4, 5]

    result = task_func(data)

    assert result.get_xlabel() == 'Letter'
    assert result.get_ylabel() == 'Count'
    assert result.get_title() == 'Letter Counts with Max Value Letter Highlighted'
    assert result.get_legend() == 'Letter Counts'

    assert result.get_xdata() == expected_letters
    assert result.get_ydata() == expected_counts

    assert result.get_bar_color(0) == 'red'
    assert result.get_bar_label(0) == 'Max Value Letter'

    assert result.get_bar_color(1) == 'red'
    assert result.get_bar_label(1) == 'Max Value Letter'

    assert result.get_bar_color(2) == 'red'
    assert result.get_bar_label(2) == 'Max Value Letter'

    assert result.get_bar_color(3) == 'red'
    assert result.get_bar_label(3) == 'Max Value Letter'

    assert result.get_bar_color(4) == 'red'
    assert result.get_bar_label(4) == 'Max Value Letter'