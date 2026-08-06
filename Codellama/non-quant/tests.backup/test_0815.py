import pytest
from src_0815 import task_func

def test_task_func_valid_input():
    source_dir = "test_data/source"
    target_dir = "test_data/target"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    moved_files_count = task_func(source_dir, target_dir, file_pattern)

    assert moved_files_count == 3
    assert os.path.exists(os.path.join(target_dir, "file1.txt"))
    assert os.path.exists(os.path.join(target_dir, "file2.doc"))
    assert os.path.exists(os.path.join(target_dir, "file3.docx"))

def test_task_func_invalid_input():
    source_dir = "test_data/source"
    target_dir = "test_data/target"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, file_pattern)

def test_task_func_invalid_file_pattern():
    source_dir = "test_data/source"
    target_dir = "test_data/target"
    file_pattern = r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'

    with pytest.raises(ValueError):
        task_func(source_dir, target_dir, file_pattern)