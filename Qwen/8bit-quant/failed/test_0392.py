import pytest
from src_0392 import task_func
import os
import tempfile
import shutil

def test_task_func_no_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result, errors = task_func(temp_dir)
        assert result is True
        assert errors == []

def test_task_func_with_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        with open(os.path.join(temp_dir, 'file1.json'), 'w') as f:
            f.write('{}')
        with open(os.path.join(temp_dir, 'file2.json'), 'w') as f:
            f.write('{}')

        result, errors = task_func(temp_dir)
        assert result is True
        assert errors == []
        assert os.path.exists(os.path.join(temp_dir, 'archive', 'file1.json'))
        assert os.path.exists(os.path.join(temp_dir, 'archive', 'file2.json'))

def test_task_func_with_permission_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Make the directory read-only
        os.chmod(temp_dir, 0o444)

        result, errors = task_func(temp_dir)
        assert result is False
        assert len(errors) == 2
        assert 'Unable to move' in errors[0]
        assert 'Unable to move' in errors[1]

        # Reset permissions
        os.chmod(temp_dir, 0o777)

def test_task_func_with_nonexistent_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        non_existent_dir = os.path.join(temp_dir, 'non_existent')
        result, errors = task_func(non_existent_dir)
        assert result is False
        assert len(errors) == 0

def test_task_func_with_archive_dir_permission_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_dir = os.path.join(temp_dir, 'archive')
        os.makedirs(archive_dir)
        os.chmod(archive_dir, 0o444)

        with open(os.path.join(temp_dir, 'file1.json'), 'w') as f:
            f.write('{}')

        result, errors = task_func(temp_dir, archive_dir=archive_dir)
        assert result is False
        assert len(errors) == 1
        assert 'Unable to move' in errors[0]

        # Reset permissions
        os.chmod(archive_dir, 0o777)