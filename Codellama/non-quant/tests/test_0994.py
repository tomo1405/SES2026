import pytest
from src_0994 import task_func

def test_task_func():
    # Test with empty string
    ax = task_func("")
    assert ax.get_xlim() == (0, 0)
    assert ax.get_ylim() == (0, 0)

    # Test with a single word
    ax = task_func("hello")
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)

    # Test with multiple words
    ax = task_func("hello world")
    assert ax.get_xlim() == (0, 2)
    assert ax.get_ylim() == (0, 2)

    # Test with a string containing non-word characters
    ax = task_func("hello, world!")
    assert ax.get_xlim() == (0, 2)
    assert ax.get_ylim() == (0, 2)

    # Test with a string containing non-word characters and multiple words
    ax = task_func("hello, world! how are you?")
    assert ax.get_xlim() == (0, 4)
    assert ax.get_ylim() == (0, 4)

    # Test with a string containing non-word characters and multiple words, and a KDE plot
    ax = task_func("hello, world! how are you?")
    assert ax.get_xlim() == (0, 4)
    assert ax.get_ylim() == (0, 4)
    assert ax.get_lines()[0].get_color() == 'red'