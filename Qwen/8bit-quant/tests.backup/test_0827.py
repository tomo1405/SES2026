import pytest
from src_0827 import task_func
import os
import tempfile

def test_task_func_no_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        assert task_func(source_dir, target_dir) == 0

def test_task_func_one_txt_file():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
            f.write('Hello, World!')
        assert task_func(source_dir, target_dir) == 1
        assert os.path.exists(os.path.join(target_dir, 'test.txt'))

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        files = ['file1.txt', 'file2.doc', 'file3.docx', 'file4.jpg']
        for file in files:
            with open(os.path.join(source_dir, file), 'w') as f:
                f.write('Content')
        assert task_func(source_dir, target_dir) == 3
        for file in files[:3]:
            assert os.path.exists(os.path.join(target_dir, file))
        for file in files[3:]:
            assert not os.path.exists(os.path.join(target_dir, file))

def test_task_func_nonexistent_source_dir():
    with tempfile.TemporaryDirectory() as target_dir:
        with pytest.raises(FileNotFoundError):
            task_func('nonexistent_dir', target_dir)

def test_task_func_target_dir_created():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as temp_dir:
        target_dir = os.path.join(temp_dir, 'new_dir')
        with open(os.path.join(source_dir, 'test.txt'), 'w') as f:
            f.write('Hello, World!')
        assert task_func(source_dir, target_dir) == 1
        assert os.path.exists(target_dir)