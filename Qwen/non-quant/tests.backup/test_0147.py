import pytest
from src_0147 import task_func
from unittest.mock import patch, call

@patch('subprocess.check_output')
def test_task_func(mock_check_output):
    mock_check_output.side_effect = [
        b'',  # Simulate successful ping
        subprocess.CalledProcessError(1, 'ping'),  # Simulate failed ping
        b'',  # Simulate successful ping
    ]
    
    ip_range = '192.168.1.0/30'
    expected_result = {
        '192.168.1.0': True,
        '192.168.1.1': False,
        '192.168.1.2': True,
        '192.168.1.3': None,  # This IP is not reachable in the given range
    }
    
    result = task_func(ip_range)
    
    assert result == expected_result
    mock_check_output.assert_has_calls([
        call('ping -c 1 192.168.1.0', shell=True),
        call('ping -c 1 192.168.1.1', shell=True),
        call('ping -c 1 192.168.1.2', shell=True),
    ])