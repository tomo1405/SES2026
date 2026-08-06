import threading

from src_0822 import task_func


def test_task_func():
    results = task_func()
    assert len(results) == 5
    for result in results:
        assert result == f'Delay in thread {threading.current_thread().name} completed'