python
import pytest
from src_0956 import task_func

def test_task_func():
    mystrings = ["apple", "banana", "cherry"]
    text = "I love apples, bananas, and cherry."
    ax = task_func(mystrings, text)
    assert isinstance(ax, plt.Axes)