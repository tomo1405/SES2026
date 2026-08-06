import pytest
from src_0032 import task_func

def test_task_func_valid_input():
    text = "This is a test sentence with $100 and $200."
    result = task_func(text)
    assert result is not None
    assert isinstance(result, matplotlib.axes.Axes)
    assert len(result.get_xticks()) == 2
    assert result.get_xticks()[0] == "100"
    assert result.get_xticks()[1] == "200"
    assert len(result.get_yticks()) == 2
    assert result.get_yticks()[0] == 1
    assert result.get_yticks()[1] == 2

def test_task_func_invalid_input():
    text = "This is a test sentence with $100 and $200."
    result = task_func(text)
    assert result is None

def test_task_func_empty_input():
    text = ""
    result = task_func(text)
    assert result is None