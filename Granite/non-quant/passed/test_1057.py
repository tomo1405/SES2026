import pytest
from src_1057 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func(n_pairs=0)
    with pytest.raises(ValueError):
        task_func(n_pairs=27)
    bars = task_func()
    assert isinstance(bars, list)
    assert len(bars) == 26