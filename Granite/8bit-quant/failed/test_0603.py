import os
import pytest
from src_0603 import task_func

def test_task_func_with_output_dir(tmp_path):
    file_path = tmp_path / "output.txt"
    task_func(file_path)
    assert file_path.exists()

def test_task_func_with_default_output_dir(monkeypatch):
    monkeypatch.setattr(task_func, "OUTPUT_DIR", "/tmp")
    file_path = "output.txt"
    task_func(file_path)
    assert os.path.exists("/tmp/output.txt")

def test_task_func_with_invalid_output_dir():
    with pytest.raises(FileNotFoundError):
        file_path = "output.txt"
        task_func(file_path, output_dir="/invalid/path")