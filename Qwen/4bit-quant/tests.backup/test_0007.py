import pytest
from src_0007 import task_func

# Mocking os and re modules to avoid file system access during testing
class MockOs:
    def listdir(self, path):
        if path == '/var/log/':
            return ['log1.txt', 'log2.log', 'log3.log']
        raise FileNotFoundError(f"No such directory: {path}")

    def path(self):
        class Path:
            def join(self, *args):
                return '/'.join(args)

            def getmtime(self, path):
                if path == '/var/log/log3.log':
                    return 3
                elif path == '/var/log/log2.log':
                    return 2
                elif path == '/var/log/log1.txt':
                    return 1
                raise FileNotFoundError(f"No such file: {path}")
        return Path()

class MockRe:
    def match(self, pattern, string):
        if pattern == r'^log\d+\.txt$' and string == 'log1.txt':
            return True
        elif pattern == r'^log\d+\.log$' and string == 'log2.log':
            return True
        elif pattern == r'^log\d+\.log$' and string == 'log3.log':
            return True
        return False

@pytest.fixture
def mock_os(monkeypatch):
    monkeypatch.setattr('src_0007.os', MockOs())

@pytest.fixture
def mock_re(monkeypatch):
    monkeypatch.setattr('src_0007.re', MockRe())

def test_task_func_with_valid_pattern(mock_os, mock_re):
    assert task_func(r'^log\d+\.txt$') == '/var/log/log1.txt'

def test_task_func_with_another_valid_pattern(mock_os, mock_re):
    assert task_func(r'^log\d+\.log$') == '/var/log/log3.log'

def test_task_func_with_no_matching_files(mock_os, mock_re):
    assert task_func(r'^nonexistent\.log$') is None

def test_task_func_with_empty_log_dir(mock_os, mock_re):
    with pytest.raises(FileNotFoundError):
        task_func(r'^log\d+\.txt$', log_dir='/nonexistent/')