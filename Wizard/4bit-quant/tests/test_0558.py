python
import pytest
from src_0558 import task_func

def test_task_func():
    s_list = ['hello', 'world', 'python']
    avg_scores = task_func(s_list)
    assert len(avg_scores) == 3
    assert isinstance(avg_scores, list)
    assert all(isinstance(score, float) for score in avg_scores)

    s_list = ['hello', 'world', 'python', 123]
    with pytest.raises(ValueError):
        task_func(s_list)

    s_list = ['hello', 'world', 'python']
    plot_path = 'plot.png'
    task_func(s_list, plot_path)
    assert plot_path.exists()

    plot_path = 'plot2.png'
    task_func(s_list, plot_path)
    assert plot_path.exists()