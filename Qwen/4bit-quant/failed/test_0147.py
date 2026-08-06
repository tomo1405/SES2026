import pytest
from src_0147 import task_func

def test_task_func_valid_ip_range():
    # Mocking the subprocess.check_output to simulate a successful ping
    def mock_check_output(*args, **kwargs):
        return b"Reply from 192.168.1.1: bytes=32 time<1ms TTL=64"

    with pytest.monkeypatch.context() as mp:
        mp.setattr(subprocess, 'check_output', mock_check_output)
        result = task_func('192.168.1.0/30')
        assert result == {
            '192.168.1.0': False,
            '192.168.1.1': True,
            '192.168.1.2': True,
            '192.168.1.3': False
        }

def test_task_func_invalid_ip_range():
    with pytest.raises(ValueError):
        task_func('invalid_ip_range')

def test_task_func_no_active_ips():
    # Mocking the subprocess.check_output to simulate a failed ping
    def mock_check_output(*args, **kwargs):
        raise subprocess.CalledProcessError(1, 'ping -c 1 192.168.1.1')

    with pytest.monkeypatch.context() as mp:
        mp.setattr(subprocess, 'check_output', mock_check_output)
        result = task_func('192.168.1.0/30')
        assert result == {
            '192.168.1.0': False,
            '192.168.1.1': False,
            '192.168.1.2': False,
            '192.168.1.3': False
        }