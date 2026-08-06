import pytest
from src_1092 import task_func

def test_task_func_no_files():
    # Create a temporary directory and ensure it's empty
    with pytest.MonkeyPatch().context() as mp:
        mp.setattr(os, 'path', '/tmp/nonexistent_directory')
        assert task_func('/tmp/nonexistent_directory') == []

def test_task_func_with_valid_files(tmp_path):
    # Create some temporary files with valid content
    (tmp_path / 'file1.txt').write_text("{'key': 'value1'}\n")
    (tmp_path / 'file2.txt').write_text("{'key': 'value2'}\n")

    expected_result = [{'key': 'value1'}, {'key': 'value2'}]
    assert task_func(str(tmp_path)) == expected_result

def test_task_func_with_invalid_content(tmp_path):
    # Create a temporary file with invalid content
    (tmp_path / 'file1.txt').write_text("invalid content\n")

    with pytest.raises(ValueError):
        task_func(str(tmp_path))

def test_task_func_with_mixed_content(tmp_path):
    # Create a temporary file with mixed valid and invalid content
    (tmp_path / 'file1.txt').write_text("{'key': 'value1'}\ninvalid content\n")

    with pytest.raises(ValueError):
        task_func(str(tmp_path))