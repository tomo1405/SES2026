import pytest
from src_0911 import task_func

def test_task_func():
    letters = ['a', 'b', 'c']
    repetitions = [1, 2, 3]
    colors = ['red', 'green', 'blue']
    ax = task_func(letters, repetitions, colors)
    assert ax.get_xlabel() == 'Letters'
    assert ax.get_ylabel() == 'Frequency'
    assert ax.get_title() == 'Frequency of Letters'
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3
    assert ax.get_xticks()[0] == 'a'
    assert ax.get_xticks()[1] == 'b'
    assert ax.get_xticks()[2] == 'c'
    assert ax.get_yticks()[0] == 1
    assert ax.get_yticks()[1] == 2
    assert ax.get_yticks()[2] == 3
    assert ax.get_xticklabels()[0].get_text() == 'a'
    assert ax.get_xticklabels()[1].get_text() == 'b'
    assert ax.get_xticklabels()[2].get_text() == 'c'
    assert ax.get_yticklabels()[0].get_text() == '1'
    assert ax.get_yticklabels()[1].get_text() == '2'
    assert ax.get_yticklabels()[2].get_text() == '3'
    assert ax.get_xticklabels()[0].get_color() == 'red'
    assert ax.get_xticklabels()[1].get_color() == 'green'
    assert ax.get_xticklabels()[2].get_color() == 'blue'
    assert ax.get_yticklabels()[0].get_color() == 'red'
    assert ax.get_yticklabels()[1].get_color() == 'green'
    assert ax.get_yticklabels()[2].get_color() == 'blue'