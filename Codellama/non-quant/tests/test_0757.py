import pytest
from src_0757 import task_func

def test_task_func_valid_input():
    source_dir = "source_dir"
    target_dir = "target_dir"
    extensions = ["txt", "pdf"]

    count = task_func(source_dir, target_dir, extensions)

    assert count == 2
    assert Path(target_dir).is_dir()
    assert Path(target_dir, "file1.txt").is_file()
    assert Path(target_dir, "file2.pdf").is_file()

def test_task_func_invalid_source_dir():
    source_dir = "invalid_dir"
    target_dir = "target_dir"
    extensions = ["txt", "pdf"]

    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, extensions)

def test_task_func_invalid_target_dir():
    source_dir = "source_dir"
    target_dir = "invalid_dir"
    extensions = ["txt", "pdf"]

    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, extensions)

def test_task_func_invalid_extensions():
    source_dir = "source_dir"
    target_dir = "target_dir"
    extensions = ["invalid_extension"]

    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, extensions)