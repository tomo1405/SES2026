import pytest
from unittest.mock import patch, call
from src_0716 import task_func

def test_task_func_defaults():
    with patch('subprocess.run') as mock_subprocess_run, \
         patch('sys.path.append') as mock_sys_path_append:
        result = task_func()
        
        mock_subprocess_run.assert_called_once_with(['pyenv', 'global', '3.8'], check=True)
        mock_sys_path_append.assert_called_once_with('/path/to/whatever')
        assert result == '3.8'

def test_task_func_custom_python_version():
    with patch('subprocess.run') as mock_subprocess_run, \
         patch('sys.path.append') as mock_sys_path_append:
        result = task_func(python_version='3.9')
        
        mock_subprocess_run.assert_called_once_with(['pyenv', 'global', '3.9'], check=True)
        mock_sys_path_append.assert_called_once_with('/path/to/whatever')
        assert result == '3.9'

def test_task_func_custom_path_to_append():
    with patch('subprocess.run') as mock_subprocess_run, \
         patch('sys.path.append') as mock_sys_path_append:
        result = task_func(path_to_append='/custom/path')
        
        mock_subprocess_run.assert_called_once_with(['pyenv', 'global', '3.8'], check=True)
        mock_sys_path_append.assert_called_once_with('/custom/path')
        assert result == '3.8'

def test_task_func_custom_both():
    with patch('subprocess.run') as mock_subprocess_run, \
         patch('sys.path.append') as mock_sys_path_append:
        result = task_func(python_version='3.9', path_to_append='/custom/path')
        
        mock_subprocess_run.assert_called_once_with(['pyenv', 'global', '3.9'], check=True)
        mock_sys_path_append.assert_called_once_with('/custom/path')
        assert result == '3.9'