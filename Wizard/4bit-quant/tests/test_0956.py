python
import pytest
from src_0956 import task_func

def test_task_func():
    mystrings = ["apple", "banana", "cherry"]
    text = "I love apple, but I hate banana and cherry."

    with pytest.raises(ValueError):
        task_func([], text)

    text = "I love apple, but I hate banana and cherry."
    ax = task_func(mystrings, text)

    assert ax.get_xlabel() == "Words"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_title() == "Word Frequency Plot"
    assert ax.get_xticklabels() == ("apple", "banana", "cherry")
    assert ax.get_xticks() == (0, 1, 2)
    assert ax.get_yticks() == (0, 1, 2, 3, 4)
    assert ax.get_ylim() == (0, 4)
    assert ax.get_xlim() == (-0.5, 2.5)