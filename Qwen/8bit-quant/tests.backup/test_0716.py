import pytest
from src_0716 import task_func
import sys
import subprocess
from unittest.mock import patch, MagicMock

@patch('subprocess.run')
@patch('sys.path.append')
def test_task_func_default_values(mock_path_append, mock_subprocess_run):
    # Arrange
    expected_python_version = '3.8'
    expected_path_to_append = '/path/to/whatever'

    # Act
    result = task_func()

    # Assert
    mock_subprocess_run.assert_called_once_with(['pyenv', 'global', expected_python_version], check=True)
    mock_path_append.assert_called_once_with(expected_path_to_append)
    assert result == expected_python_version

@patch('subprocess.run')
@patch('sys.path.append')
def test_task_func_custom_values(mock_path_append, mock_subprocess_run):
    # Arrange
    custom_python_version = '3.9'
    custom_path_to_append = '/another/path'

    # Act
    result = task_func(custom_python_version, custom_path_to_append)

    # Assert
    mock_subprocess_run.assert_called_once_with(['pyenv', 'global', custom_python_version], check=True)
    mock_path_append.assert_called_once_with(custom_path_to_append)
    assert result == custom_python_version

@patch('subprocess.run', side_effect=subprocess.CalledProcessError(1, ['pyenv', 'global']))
def test_task_func_subprocess_error(mock_subprocess_run):
    # Arrange
    with pytest.raises(subprocess.CalledProcessError):
        # Act
        task_func()