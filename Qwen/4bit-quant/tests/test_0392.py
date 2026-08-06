import pytest
from src_0392 import task_func
import os
import tempfile

def test_task_func_no_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_dir = os.path.join(temp_dir, 'archive')
        result, error_messages = task_func(temp_dir, archive_dir)
        assert result is True
        assert error_messages == []
        assert not os.path.exists(archive_dir)

def test_task_func_with_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_dir = os.path.join(temp_dir, 'archive')
        json_file_path = os.path.join(temp_dir, 'test.json')
        with open(json_file_path, 'w') as f:
            f.write('{"key": "value"}')

        result, error_messages = task_func(temp_dir, archive_dir)
        assert result is True
        assert error_messages == []
        assert os.path.exists(archive_dir)
        assert os.path.exists(os.path.join(archive_dir, 'test.json'))

def test_task_func_with_permission_error():
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_dir = os.path.join(temp_dir, 'archive')
        json_file_path = os.path.join(temp_dir, 'test.json')
        with open(json_file_path, 'w') as f:
            f.write('{"key": "value"}')

        # Make the directory read-only
        os.chmod(temp_dir, 0o444)

        result, error_messages = task_func(temp_dir, archive_dir)
        assert result is False
        assert len(error_messages) == 1
        assert 'Unable to move' in error_messages[0]

        # Reset permissions for cleanup
        os.chmod(temp_dir, 0o777)

def test_task_func_with_non_existent_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        archive_dir = os.path.join(temp_dir, 'archive')
        non_existent_dir = os.path.join(temp_dir, 'non_existent')
        json_file_path = os.path.join(non_existent_dir, 'test.json')
        os.makedirs(non_existent_dir)
        with open(json_file_path, 'w') as f:
            f.write('{"key": "value"}')

        # Remove the directory to make it non-existent
        os.rmdir(non_existent_dir)

        result, error_messages = task_func(non_existent_dir, archive_dir)
        assert result is False
        assert len(error_messages) == 1
        assert 'No such file or directory' in error_messages[0]