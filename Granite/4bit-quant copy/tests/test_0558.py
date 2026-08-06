import pytest
from src_0558 import task_func

def test_task_func():
    s_list = ["abc", "def", "ghi"]
    avg_scores = task_func(s_list)
    assert isinstance(avg_scores, list)
    assert len(avg_scores) == len(s_list)
    for score in avg_scores:
        assert isinstance(score, float)
    with pytest.raises(ValueError):
        task_func(["abc", 123])