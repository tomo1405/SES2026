import logging
import subprocess
import tempfile

import pytest
from src_0605 import task_func


# Mocking subprocess and logging for testing
class MockSubprocess:
    def check_call(self, args):
        if args[1] == 'non_existent_file.cpp':
            raise FileNotFoundError("File not found")
        elif args[1] == 'compilation_error.cpp':
            raise subprocess.CalledProcessError(1, args)

    def __getattr__(self, name):
        return lambda *args, **kwargs: None

@pytest.fixture
def mock_subprocess(monkeypatch):
    monkeypatch.setattr(subprocess, 'check_call', MockSubprocess().check_call)

@pytest.fixture
def setup_logging():
    # Set up logging to capture messages
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    logger.handlers.clear()  # Clear existing handlers
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def test_successful_compilation(mock_subprocess, setup_logging, caplog):
    with tempfile.NamedTemporaryFile(suffix='.cpp') as temp_file:
        temp_file.write(b'int main() { return 0; }')
        temp_file.flush()
        task_func(temp_file.name)
        assert "Successfully compiled" in caplog.text

def test_file_not_found(mock_subprocess, setup_logging, caplog):
    task_func('non_existent_file.cpp')
    assert "File not found" in caplog.text

def test_compilation_error(mock_subprocess, setup_logging, caplog):
    task_func('compilation_error.cpp')
    assert "Failed to compile" in caplog.text