import pytest
from src_0558 import task_func

def test_task_func_valid_input():
    s_list = ["apple", "banana", "orange"]
    avg_scores = task_func(s_list)
    assert isinstance(avg_scores, list)
    assert len(avg_scores) == len(s_list)

def test_task_func_invalid_input():
    s_list = [1, 2, 3]
    with pytest.raises(ValueError):
        task_func(s_list)

def test_task_func_plot():
    s_list = ["apple", "banana", "orange"]
    plot_path = "plot.png"
    task_func(s_list, plot_path)
    assert os.path.exists(plot_path)
    os.remove(plot_path)