import pytest
from src_0558 import task_func

def test_task_func_valid_input():
    s_list = ["apple", "banana", "orange"]
    plot_path = "test_plot.png"
    expected_avg_scores = [0.5, 0.6, 0.7]

    avg_scores = task_func(s_list, plot_path)

    assert avg_scores == expected_avg_scores
    assert plt.bar(s_list, avg_scores)
    assert plt.savefig(plot_path)

def test_task_func_invalid_input():
    s_list = ["apple", "banana", 1]
    plot_path = "test_plot.png"

    with pytest.raises(ValueError):
        task_func(s_list, plot_path)