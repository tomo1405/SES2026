import pytest
from src_0392 import task_func
import os
import tempfile

def test_task_func_no_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_dir = os.path.join(temp_dir, 'archive')
        result, errors = task_func(temp_dir, archive_dir)
        assert result is True
        assert errors == []
        assert not os.path.exists(archive_dir)

def test_task_func_with_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        json_file1 = os.path.join(temp_dir, 'file1.json')
        json_file2 = os.path.join(temp_dir, 'file2.json')
        with open(json_file1, 'w') as f:
            f.write('{"key": "value"}')
        with open(json_file2, 'w') as f:
            f.write('{"key": "value"}')

        archive_dir = os.path.join(temp_dir, 'archive')
        result, errors = task_func(temp_dir, archive_dir)
        assert result is True
        assert errors == []
        assert os.path.exists(archive_dir)
        assert os.path.exists(os.path.join(archive_dir, 'file1.json'))
        assert os.path.exists(os.path.join(archive_dir, 'file2.json'))

def test_task_func_permission_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        json_file = os.path.join(temp_dir, 'file1.json')
        with open(json_file, 'w') as f:
            f.write('{"key": "value"}')

        archive_dir = os.path.join(temp_dir, 'archive')
        os.chmod(archive_dir, 0o000)  # Make archive directory non-writable

        result, errors = task_func(temp_dir, archive_dir)
        assert result is False
        assert len(errors) == 1
        assert 'Permission denied' in errors[0]

        os.chmod(archive_dir, 0o755)  # Restore permissions

def test_task_func_nonexistent_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_dir = os.path.join(temp_dir, 'nonexistent_archive')
        result, errors = task_func(temp_dir, archive_dir)
        assert result is True
        assert errors == []
        assert os.path.exists(archive_dir)