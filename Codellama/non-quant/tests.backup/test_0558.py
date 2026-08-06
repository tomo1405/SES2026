import pytest
from src_0558 import task_func

def test_task_func_valid_input():
    s_list = ["apple", "banana", "cherry"]
    plot_path = "test_plot.png"
    avg_scores = task_func(s_list, plot_path)
    assert isinstance(avg_scores, list)
    assert len(avg_scores) == len(s_list)
    assert all(isinstance(score, float) for score in avg_scores)
    assert all(score >= 0 for score in avg_scores)
    assert all(score <= 1 for score in avg_scores)

def test_task_func_invalid_input():
    s_list = ["apple", "banana", 1]
    plot_path = "test_plot.png"
    with pytest.raises(ValueError):
        task_func(s_list, plot_path)

def test_task_func_plot_path():
    s_list = ["apple", "banana", "cherry"]
    plot_path = "test_plot.png"
    task_func(s_list, plot_path)
    assert os.path.exists(plot_path)
    os.remove(plot_path)