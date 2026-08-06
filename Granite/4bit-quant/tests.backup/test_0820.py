import pytest
from src_0820 import task_func

def test_task_func():
    messages, total_delay = task_func()
    assert isinstance(messages, list)
    assert isinstance(total_delay, (int, float))
    assert len(messages) > 0
    for message in messages:
        assert isinstance(message, str)

def test_task_func_iterations():
    with pytest.raises(ValueError):
        task_func(iterations='foo')
    with pytest.raises(ValueError):
        task_func(iterations=-1)

def test_task_func_delays():
    with pytest.raises(ValueError):
        task_func(min_delay='foo')
    with pytest.raises(ValueError):
        task_func(min_delay=0)
    with pytest.raises(ValueError):
        task_func(max_delay='foo')
    with pytest.raises(ValueError):
        task_func(max_delay=1)
    with pytest.raises(ValueError):
        task_func(max_delay=1, min_delay=2)