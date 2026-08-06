import pytest
from src_0769 import task_func

def test_task_func_non_existent_directory():
    with pytest.raises(ValueError, match="Specified directory does not exist."):
        task_func('/non/existent/directory')

def test_task_func_empty_directory(tmp_path):
    assert task_func(str(tmp_path)) == {}

def test_task_func_single_file_no_errors(tmp_path):
    (tmp_path / 'file.txt').write_text('This is a test file without errors.')
    assert task_func(str(tmp_path)) == {'file.txt': 0}

def test_task_func_single_file_with_errors(tmp_path):
    (tmp_path / 'file.txt').write_text('This is a test file with one error and another Error.')
    assert task_func(str(tmp_path)) == {'file.txt': 2}

def test_task_func_multiple_files(tmp_path):
    (tmp_path / 'file1.txt').write_text('This is file1 with no errors.')
    (tmp_path / 'file2.txt').write_text('This is file2 with one error and another Error.')
    (tmp_path / 'subdir' / 'file3.txt').mkdir(parents=True)
    (tmp_path / 'subdir' / 'file3.txt').write_text('This is file3 with three errors, Error, error, and ERROR.')
    expected_result = {
        'file1.txt': 0,
        'file2.txt': 2,
        'subdir/file3.txt': 3
    }
    assert task_func(str(tmp_path)) == expected_result

def test_task_func_case_insensitivity(tmp_path):
    (tmp_path / 'file.txt').write_text('Error error ERROR')
    assert task_func(str(tmp_path)) == {'file.txt': 3}