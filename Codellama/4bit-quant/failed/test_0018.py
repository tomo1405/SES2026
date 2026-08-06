import pytest
from src_0018 import task_func

def test_task_func():
    # Test case 1: Process is running
    process_name = "python"
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    assert is_running
    result = task_func(process_name)
    assert result == f"Process found. Restarting {process_name}."

    # Test case 2: Process is not running
    process_name = "python"
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    assert not is_running
    result = task_func(process_name)
    assert result == f"Process not found. Starting {process_name}."

    # Test case 3: Process is running, but cannot be terminated
    process_name = "python"
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    assert is_running
    with pytest.raises(Exception):
        task_func(process_name)

    # Test case 4: Process is not running, but cannot be started
    process_name = "python"
    is_running = any([proc for proc in psutil.process_iter() if proc.name() == process_name])
    assert not is_running
    with pytest.raises(Exception):
        task_func(process_name)