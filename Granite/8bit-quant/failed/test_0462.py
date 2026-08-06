import pytest
from src_0462 import task_func

def test_task_func():
    script_path = "path/to/script.sh"
    timeout = 10
    expected_output = {"CPU Usage": 50.0, "Memory Usage": 1000000}

    with pytest.raises(FileNotFoundError):
        task_func("invalid_path", timeout)

    output = task_func(script_path, timeout)
    assert output == expected_output