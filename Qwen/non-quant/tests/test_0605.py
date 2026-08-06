import pytest
from src_0605 import task_func
import subprocess
import logging
import os

# Mocking subprocess and logging for testing
class MockSubprocess:
    def check_call(self, args):
        if 'non_existent_file.cpp' in args:
            raise subprocess.CalledProcessError(1, args)
        elif 'missing_compiler.cpp' in args:
            raise FileNotFoundError("Compiler not found")
        return 0

class MockLogger:
    def __init__(self):
        self.logs = []

    def info(self, msg, *args):
        self.logs.append((logging.INFO, msg % args))

    def error(self, msg, *args):
        self.logs.append((logging.ERROR, msg % args))

@pytest.fixture
def mock_subprocess(monkeypatch):
    mock = MockSubprocess()
    monkeypatch.setattr(subprocess, 'check_call', mock.check_call)
    return mock

@pytest.fixture
def mock_logger(monkeypatch):
    mock = MockLogger()
    monkeypatch.setattr(logging, 'basicConfig', lambda level: None)
    monkeypatch.setattr(logging, 'info', mock.info)
    monkeypatch.setattr(logging, 'error', mock.error)
    return mock

def test_successful_compilation(mock_subprocess, mock_logger, tmp_path):
    # Create a temporary C++ file
    cpp_file = tmp_path / "test_success.cpp"
    cpp_file.write_text("int main() { return 0; }")

    task_func(str(cpp_file))

    assert mock_logger.logs == [
        (logging.INFO, 'Successfully compiled %s' % str(cpp_file))
    ]

def test_failed_compilation(mock_subprocess, mock_logger, tmp_path):
    # Create a temporary C++ file with a syntax error
    cpp_file = tmp_path / "test_failure.cpp"
    cpp_file.write_text("int main() { return; }")  # Missing return value

    task_func(str(cpp_file))

    assert mock_logger.logs == [
        (logging.ERROR, 'Failed to compile %s: %s' % (str(cpp_file), subprocess.CalledProcessError(1, ['g++', str(cpp_file), '-o', 'test_failure'])))
    ]

def test_missing_compiler(mock_subprocess, mock_logger, tmp_path):
    # Create a temporary C++ file
    cpp_file = tmp_path / "missing_compiler.cpp"
    cpp_file.write_text("int main() { return 0; }")

    task_func(str(cpp_file))

    assert mock_logger.logs == [
        (logging.ERROR, 'Compiler not found or file does not exist: %s' % FileNotFoundError("Compiler not found"))
    ]