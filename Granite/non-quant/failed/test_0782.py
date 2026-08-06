import os
from datetime import datetime
from unittest.mock import patch

import pytest

from src_0782 import task_func

def test_task_func():
    with patch('os.path.getsize') as mock_getsize, patch('os.path.getmtime') as mock_getmtime:
        mock_getsize.return_value = 1024
        mock_getmtime.return_value = 1634616324.123456

        result = task_func('test_file.txt')

        mock_getsize.assert_called_once_with('test_file.txt')
        mock_getmtime.assert_called_once_with('test_file.txt')
        assert result == {'size': '1024 bytes', 'last_modified': '2021-10-19 18:05:24'}

def test_task_func_with_oserror():
    with patch('os.path.getsize') as mock_getsize, patch('os.path.getmtime') as mock_getmtime, pytest.raises(Exception) as exc_info:
        mock_getsize.return_value = 1024
        mock_getmtime.side_effect = OSError('Test error')

        task_func('test_file.txt')

        mock_getsize.assert_called_once_with('test_file.txt')
        mock_getmtime.assert_called_once_with('test_file.txt')
        assert str(exc_info.value) == 'Error: Test error'