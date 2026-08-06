import pytest
from src_0815 import task_func

def test_task_func():
    source_dir = "source_dir"
    target_dir = "target_dir"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    # Test case 1: source directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, file_pattern)

    # Test case 2: target directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, file_pattern)

    # Test case 3: source directory exists, target directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, file_pattern)

    # Test case 4: source directory exists, target directory exists, file pattern matches
    source_dir = "source_dir"
    target_dir = "target_dir"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count == 1

    # Test case 5: source directory exists, target directory exists, file pattern does not match
    source_dir = "source_dir"
    target_dir = "target_dir"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'
    moved_files_count = task_func(source_dir, target_dir, file_pattern)
    assert moved_files_count == 0