import pytest
from src_0013 import task_func

def test_task_func_valid_script():
    log_data = task_func('backup.sh')
    assert log_data['start_time'] == '2023-02-21 12:00:00'
    assert log_data['end_time'] == '2023-02-21 12:00:01'
    assert log_data['exit_status'] == 0

def test_task_func_invalid_script():
    with pytest.raises(FileNotFoundError):
        task_func('invalid_script.sh')

def test_task_func_exception():
    with pytest.raises(RuntimeError):
        task_func('error_script.sh')