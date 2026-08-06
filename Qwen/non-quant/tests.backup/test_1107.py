import pytest
from src_1107 import task_func
from datetime import datetime
from pathlib import Path
import os

# Mocking os.path.getctime and Path.exists to avoid actual file system operations
class TestTaskFunc:
    def test_file_not_found(self, monkeypatch):
        def mock_exists(path):
            return False
        
        monkeypatch.setattr(Path, 'exists', mock_exists)
        
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func('non_existent_file.txt')
        
        assert str(excinfo.value) == "No such file or directory: 'non_existent_file.txt'"

    def test_valid_file(self, monkeypatch):
        def mock_exists(path):
            return True
        
        def mock_getctime(path):
            return 1633072800  # Example timestamp for 2021-10-01 00:00:00
        
        monkeypatch.setattr(Path, 'exists', mock_exists)
        monkeypatch.setattr(os.path, 'getctime', mock_getctime)
        
        result = task_func('valid_file.txt')
        expected_time = datetime.fromtimestamp(1633072800).strftime('%Y-%m-%d %H:%M:%S')
        assert result == expected_time