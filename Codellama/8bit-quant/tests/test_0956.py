import pytest
from src_0956 import task_func

def test_task_func_empty_text():
    with pytest.raises(ValueError):
        task_func([], "")

def test_task_func_valid_text():
    text = "This is a test text"
    mystrings = ["test", "is"]
    ax = task_func(mystrings, text)
    assert ax.get_xticks() == [0, 1]
    assert ax.get_xticklabels() == ["test", "is"]
    assert ax.get_yticks() == [1, 2]
    assert ax.get_yticklabels() == ["This", "a"]