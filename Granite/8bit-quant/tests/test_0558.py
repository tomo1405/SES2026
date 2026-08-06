import pytest
from src_0558 import task_func

def test_task_func():
    s_list = ["abc", "def", "ghi"]
    avg_scores = task_func(s_list)
    assert isinstance(avg_scores, list)
    assert len(avg_scores) == len(s_list)
    for score in avg_scores:
        assert isinstance(score, float)

def test_task_func_with_plot():
    s_list = ["abc", "def", "ghi"]
    plot_path = "plot.png"
    avg_scores = task_func(s_list, plot_path)
    assert isinstance(avg_scores, list)
    assert len(avg_scores) == len(s_list)
    for score in avg_scores:
        assert isinstance(score, float)
    assert "plot.png" in plot_path

def test_task_func_with_invalid_input():
    s_list = [1, 2, 3]
    with pytest.raises(ValueError) as excinfo:
        task_func(s_list)
    assert "All items in s_list must be strings." in str(excinfo.value)