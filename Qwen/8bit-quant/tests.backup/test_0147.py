import pytest
from src_0147 import task_func
from unittest.mock import patch

def test_task_func_valid_ip_range():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.return_value = b''
        result = task_func('192.168.1.0/30')
        expected = {
            '192.168.1.0': True,
            '192.168.1.1': True,
            '192.168.1.2': True,
            '192.168.1.3': True
        }
        assert result == expected

def test_task_func_invalid_ip_range():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.return_value = b''
        result = task_func('invalid_ip_range')
        assert result == {}

def test_task_func_some_ips_inactive():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.side_effect = [
            b'',  # Successful ping for 192.168.1.0
            subprocess.CalledProcessError(1, ''),  # Failed ping for 192.168.1.1
            b'',  # Successful ping for 192.168.1.2
            subprocess.CalledProcessError(1, '')  # Failed ping for 192.168.1.3
        ]
        result = task_func('192.168.1.0/30')
        expected = {
            '192.168.1.0': True,
            '192.168.1.1': False,
            '192.168.1.2': True,
            '192.168.1.3': False
        }
        assert result == expected

def test_task_func_single_ip():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.return_value = b''
        result = task_func('192.168.1.1/32')
        expected = {'192.168.1.1': True}
        assert result == expected

def test_task_func_single_ip_inactive():
    with patch('subprocess.check_output') as mock_check_output:
        mock_check_output.side_effect = subprocess.CalledProcessError(1, '')
        result = task_func('192.168.1.1/32')
        expected = {'192.168.1.1': False}
        assert result == expected