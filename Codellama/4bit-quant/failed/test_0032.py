import pytest
from src_0032 import task_func

def test_task_func():
    text = "This is a test sentence with $100 and $200."
    result = task_func(text)
    assert result is not None
    assert isinstance(result, matplotlib.axes.Axes)
    assert result.get_xlabel() == "Dollar Amount"
    assert result.get_ylabel() == "Frequency"
    assert result.get_title() == "Dollar Amount Distribution"
    assert result.get_xlim() == (0, 100)
    assert result.get_ylim() == (0, 100)
    assert result.get_xticks() == [0, 25, 50, 75, 100]
    assert result.get_yticks() == [0, 25, 50, 75, 100]
    assert result.get_xticklabels() == ["$0", "$25", "$50", "$75", "$100"]
    assert result.get_yticklabels() == ["0", "25", "50", "75", "100"]