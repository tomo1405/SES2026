import pytest
from unittest.mock import patch, MagicMock
from src_0018 import task_func

def test_task_func_process_running():
    process_name = "example_process"
    with patch('psutil.process_iter') as mock_process_iter:
        mock_process_iter.return_value = [MagicMock(name=process_name)]
        with patch('subprocess.Popen') as mock_popen:
            with patch('time.sleep'):
                result = task_func(process_name)
                mock_popen.assert_called_once_with(process_name)
                assert result == f"Process found. Restarting {process_name}."

def test_task_func_process_not_running():
    process_name = "example_process"
    with patch('psutil.process_iter') as mock_process_iter:
        mock_process_iter.return_value = []
        with patch('subprocess.Popen') as mock_popen:
            result = task_func(process_name)
            mock_popen.assert_called_once_with(process_name)
            assert result == f"Process not found. Starting {process_name}."