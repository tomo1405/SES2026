import pytest
from src_0455 import task_func
import os
import tempfile
import shutil

def test_task_func_no_files_found():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        ext = 'txt'
        assert task_func(src_dir, dest_dir, ext) == []

def test_task_func_files_found():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        ext = 'txt'
        file1 = os.path.join(src_dir, f'test1.{ext}')
        file2 = os.path.join(src_dir, f'test2.{ext}')
        with open(file1, 'w') as f:
            f.write('content1')
        with open(file2, 'w') as f:
            f.write('content2')

        moved_files = task_func(src_dir, dest_dir, ext)
        assert len(moved_files) == 2
        assert os.path.exists(os.path.join(dest_dir, f'test1.{ext}'))
        assert os.path.exists(os.path.join(dest_dir, f'test2.{ext}'))

def test_task_func_source_directory_not_exists():
    with tempfile.TemporaryDirectory() as dest_dir:
        src_dir = 'non_existent_src'
        ext = 'txt'
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func(src_dir, dest_dir, ext)
        assert str(excinfo.value) == f"Source directory '{src_dir}' does not exist."

def test_task_func_destination_directory_not_exists():
    with tempfile.TemporaryDirectory() as src_dir:
        dest_dir = 'non_existent_dest'
        ext = 'txt'
        with pytest.raises(FileNotFoundError) as excinfo:
            task_func(src_dir, dest_dir, ext)
        assert str(excinfo.value) == f"Destination directory '{dest_dir}' does not exist."

def test_task_func_file_already_exists():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dest_dir:
        ext = 'txt'
        file1 = os.path.join(src_dir, f'test1.{ext}')
        file2 = os.path.join(dest_dir, f'test1.{ext}')
        with open(file1, 'w') as f:
            f.write('content1')
        with open(file2, 'w') as f:
            f.write('content2')

        moved_files = task_func(src_dir, dest_dir, ext)
        assert len(moved_files) == 0
        assert os.path.exists(os.path.join(dest_dir, f'test1.{ext}'))
        assert not os.path.exists(os.path.join(src_dir, f'test1.{ext}'))