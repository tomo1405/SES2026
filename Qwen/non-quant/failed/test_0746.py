import pytest
from src_0746 import task_func
import os
from unittest.mock import patch, call

@pytest.fixture
def mock_subprocess_call(mocker):
    return mocker.patch('src_0746.subprocess.call')

@pytest.fixture
def mock_random_choice(mocker):
    return mocker.patch('src_0746.random.choice')

def test_task_func(mock_subprocess_call, mock_random_choice):
    # Arrange
    expected_script_name = 'script1.sh'
    mock_random_choice.return_value = expected_script_name
    expected_script_path = os.path.join('/path/to/scripts', expected_script_name)

    # Act
    result = task_func()

    # Assert
    assert result == expected_script_path
    mock_random_choice.assert_called_once_with(['script1.sh', 'script2.sh', 'script3.sh'])
    mock_subprocess_call.assert_called_once_with(expected_script_path, shell=True)