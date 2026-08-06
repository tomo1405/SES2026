import pytest
from src_0162 import task_func

def test_task_func():
    log_file = 'test_log.log'
    output_csv_path = task_func(log_file)
    assert output_csv_path == 'log_data.csv'

def test_task_func_invalid_log_file():
    log_file = 'invalid_log.log'
    with pytest.raises(ValueError):
        task_func(log_file)

def test_task_func_invalid_timestamp():
    log_file = 'test_log.log'
    with open(log_file, 'w') as file:
        file.write('ERROR: [2022-01-01 12:00:00] - Invalid timestamp')
    with pytest.raises(ValueError):
        task_func(log_file)

def test_task_func_no_valid_log_entries():
    log_file = 'test_log.log'
    with open(log_file, 'w') as file:
        file.write('ERROR: [2022-01-01 12:00:00] - Invalid timestamp')
    with pytest.raises(ValueError):
        task_func(log_file)