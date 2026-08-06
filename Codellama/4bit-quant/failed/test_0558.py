import pytest
from src_0558 import task_func

def test_task_func():
    s_list = ["apple", "banana", "cherry"]
    plot_path = "test_plot.png"
    avg_scores = task_func(s_list, plot_path)
    assert all(isinstance(score, float) for score in avg_scores)
    assert len(avg_scores) == len(s_list)
    assert avg_scores[0] == 1.0
    assert avg_scores[1] == 0.5
    assert avg_scores[2] == 0.0
    assert plt.bar(s_list, avg_scores)
    assert plt.savefig(plot_path)