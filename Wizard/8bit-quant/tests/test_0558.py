python
import pytest
from src_0558 import task_func

def test_task_func():
    s_list = ['hello', 'world', 'python']
    avg_scores = task_func(s_list)
    assert len(avg_scores) == len(s_list)
    assert all(0 <= score <= 1 for score in avg_scores)

    s_list = ['hello', 'world', 'python', 'hello']
    with pytest.raises(ValueError):
        task_func(s_list)

    s_list = ['hello', 'world', 'python']
    plot_path = 'test.png'
    task_func(s_list, plot_path)
    assert plot_path.exists()
    plot_path.unlink()