import pytest
from src_0119 import task_func
import os
import tempfile

def test_task_func_no_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        backup_dir = os.path.join(temp_dir, 'backup')
        result = task_func(temp_dir, backup_dir)
        assert result == []

def test_task_func_with_json_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        backup_dir = os.path.join(temp_dir, 'backup')
        json_file1 = os.path.join(temp_dir, 'file1.json')
        json_file2 = os.path.join(temp_dir, 'file2.json')
        
        with open(json_file1, 'w') as f:
            f.write('{}')
        with open(json_file2, 'w') as f:
            f.write('{}')
        
        result = task_func(temp_dir, backup_dir)
        expected = [os.path.join(backup_dir, 'file1.json'), os.path.join(backup_dir, 'file2.json')]
        assert sorted(result) == sorted(expected)

def test_task_func_backup_directory_exists():
    with tempfile.TemporaryDirectory() as temp_dir:
        backup_dir = os.path.join(temp_dir, 'backup')
        os.makedirs(backup_dir)
        
        json_file = os.path.join(temp_dir, 'file.json')
        with open(json_file, 'w') as f:
            f.write('{}')
        
        result = task_func(temp_dir, backup_dir)
        assert result == [os.path.join(backup_dir, 'file.json')]

def test_task_func_nonexistent_source_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        backup_dir = os.path.join(temp_dir, 'backup')
        non_existent_dir = os.path.join(temp_dir, 'non_existent')
        
        result = task_func(non_existent_dir, backup_dir)
        assert result == []

def test_task_func_empty_backup_directory_name():
    with tempfile.TemporaryDirectory() as temp_dir:
        backup_dir = ''
        json_file = os.path.join(temp_dir, 'file.json')
        with open(json_file, 'w') as f:
            f.write('{}')
        
        result = task_func(temp_dir, backup_dir)
        assert result == [os.path.join(temp_dir, 'file.json')]