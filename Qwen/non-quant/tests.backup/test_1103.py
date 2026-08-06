import pytest
from src_1103 import task_func
from unittest.mock import patch, Mock

@patch('subprocess.Popen')
def test_task_func(mock_popen):
    # Arrange
    script_path = "test_script.R"
    mock_process = Mock()
    mock_popen.return_value = mock_process
    mock_process.communicate.return_value = (b"stdout", b"stderr")
    mock_process.returncode = 0

    # Act
    result = task_func(script_path)

    # Assert
    assert isinstance(result, dict)
    assert 'Start Time' in result
    assert 'End Time' in result
    assert 'Stdout' in result
    assert 'Stderr' in result
    assert result['Stdout'] == "stdout"
    assert result['Stderr'] == "stderr"

@patch('subprocess.Popen')
def test_task_func_with_error(mock_popen):
    # Arrange
    script_path = "test_script.R"
    mock_process = Mock()
    mock_popen.return_value = mock_process
    mock_process.communicate.return_value = (b"stdout", b"stderr")
    mock_process.returncode = 1

    # Act & Assert
    with pytest.raises(Exception):
        task_func(script_path)

@patch('subprocess.Popen')
def test_task_func_with_no_output(mock_popen):
    # Arrange
    script_path = "test_script.R"
    mock_process = Mock()
    mock_popen.return_value = mock_process
    mock_process.communicate.return_value = (b"", b"")

    # Act
    result = task_func(script_path)

    # Assert
    assert result['Stdout'] == ""
    assert result['Stderr'] == ""

@patch('subprocess.Popen')
def test_task_func_with_nonexistent_script(mock_popen):
    # Arrange
    script_path = "nonexistent_script.R"
    mock_process = Mock()
    mock_popen.return_value = mock_process
    mock_process.communicate.return_value = (b"", b"Error: File does not exist")

    # Act
    result = task_func(script_path)

    # Assert
    assert result['Stderr'] == "Error: File does not exist"