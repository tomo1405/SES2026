import pytest
from src_0013 import task_func

def test_task_func():
    script_name = 'backup.sh'
    log_file = '/home/user/backup_log.json'
    log_data = task_func(script_name, log_file)
    assert log_data['start_time'] == datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    assert log_data['end_time'] == datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    assert log_data['exit_status'] == 0
    assert os.path.isfile(log_file)
    with open(log_file, 'r') as f:
        log_data = json.load(f)
        assert log_data['start_time'] == datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        assert log_data['end_time'] == datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        assert log_data['exit_status'] == 0