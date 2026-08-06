import pytest
from src_1135 import task_func
import os
import tempfile

def test_task_func_nonexistent_source_dir():
    with tempfile.TemporaryDirectory() as target_dir:
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func('nonexistent_source_dir', target_dir)
        assert "Source directory 'nonexistent_source_dir' does not exist." in str(excinfo.value)

def test_task_func_empty_source_dir():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            result = task_func(source_dir, target_dir)
            assert result == []

def test_task_func_single_file():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            source_file_path = os.path.join(source_dir, 'test.txt')
            with open(source_file_path, 'w') as f:
                f.write('Hello, World!')
            
            result = task_func(source_dir, target_dir)
            assert len(result) == 1
            target_file_path = result[0]
            assert os.path.basename(target_file_path) == 'test.txt'
            
            with open(target_file_path, 'r') as f:
                lines = f.readlines()
                assert len(lines) == 2
                assert lines[0].startswith('#Hash: ')
                assert lines[1] == 'Hello, World!\n'

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            file_paths = [
                os.path.join(source_dir, 'file1.txt'),
                os.path.join(source_dir, 'file2.txt')
            ]
            for file_path in file_paths:
                with open(file_path, 'w') as f:
                    f.write(f'Content of {os.path.basename(file_path)}')
            
            result = task_func(source_dir, target_dir)
            assert len(result) == 2
            for target_file_path in result:
                assert os.path.basename(target_file_path) in ['file1.txt', 'file2.txt']
                with open(target_file_path, 'r') as f:
                    lines = f.readlines()
                    assert len(lines) == 2
                    assert lines[0].startswith('#Hash: ')
                    assert lines[1].endswith('\n')

def test_task_func_custom_prefix():
    with tempfile.TemporaryDirectory() as source_dir:
        with tempfile.TemporaryDirectory() as target_dir:
            source_file_path = os.path.join(source_dir, 'test.txt')
            with open(source_file_path, 'w') as f:
                f.write('Hello, World!')
            
            custom_prefix = '#CustomPrefix: '
            result = task_func(source_dir, target_dir, prefix=custom_prefix)
            assert len(result) == 1
            target_file_path = result[0]
            assert os.path.basename(target_file_path) == 'test.txt'
            
            with open(target_file_path, 'r') as f:
                lines = f.readlines()
                assert len(lines) == 2
                assert lines[0].startswith(custom_prefix)
                assert lines[1] == 'Hello, World!\n'