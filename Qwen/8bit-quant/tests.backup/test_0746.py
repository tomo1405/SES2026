import pytest
from src_0746 import task_func
import os
from unittest.mock import patch, call

@pytest.fixture
def mock_random_choice(monkeypatch):
    def choice(seq):
        return seq[0]  # Always return the first element in the list
    monkeypatch.setattr(random, 'choice', choice)

@pytest.fixture
def mock_subprocess_call(monkeypatch):
    mock_call = mock.Mock()
    monkeypatch.setattr(subprocess, 'call', mock_call)
    return mock_call

def test_task_func(mock_random_choice, mock_subprocess_call):
    expected_script = 'script1.sh'
    expected_path = os.path.join('/path/to/scripts', expected_script)
    
    result = task_func()
    
    assert result == expected_path
    mock_subprocess_call.assert_called_once_with(expected_path, shell=True)