import pytest
from src_0956 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func([], "")

    mystrings = ["hello", "world"]
    text = "Hello, world!"
    ax = task_func(mystrings, text)

    assert ax is not None
    assert ax.get_xticks() is not None
    assert ax.get_xticklabels() is not None