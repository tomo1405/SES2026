import pytest
from src_0666 import task_func
import shutil
import os
import tempfile

def test_task_func_no_matching_files():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        # Create some files that do not match the patterns
        open(os.path.join(src_dir, 'file.jpg'), 'w').close()
        open(os.path.join(src_dir, 'image.png'), 'w').close()

        result = task_func(src_dir, dst_dir)
        assert result == dst_dir
        assert not os.listdir(dst_dir)

def test_task_func_with_matching_files():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        # Create some files that match the patterns
        open(os.path.join(src_dir, 'document.txt'), 'w').close()
        open(os.path.join(src_dir, 'notes.docx'), 'w').close()

        result = task_func(src_dir, dst_dir)
        assert result == dst_dir
        assert set(os.listdir(dst_dir)) == {'document.txt', 'notes.docx'}

def test_task_func_with_subdirectories():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        # Create subdirectories and files
        subdir = os.path.join(src_dir, 'subdir')
        os.makedirs(subdir)
        open(os.path.join(subdir, 'report.txt'), 'w').close()
        open(os.path.join(src_dir, 'summary.docx'), 'w').close()

        result = task_func(src_dir, dst_dir)
        assert result == dst_dir
        assert set(os.listdir(dst_dir)) == {'summary.docx'}
        assert not os.listdir(subdir)  # Ensure no files were copied from subdirectories

def test_task_func_empty_source_directory():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        # Source directory is empty
        result = task_func(src_dir, dst_dir)
        assert result == dst_dir
        assert not os.listdir(dst_dir)

def test_task_func_dst_directory_exists():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        # Destination directory already exists
        open(os.path.join(src_dir, 'document.txt'), 'w').close()
        open(os.path.join(src_dir, 'notes.docx'), 'w').close()

        result = task_func(src_dir, dst_dir)
        assert result == dst_dir
        assert set(os.listdir(dst_dir)) == {'document.txt', 'notes.docx'}

def test_task_func_dst_directory_not_exists():
    with tempfile.TemporaryDirectory() as src_dir:
        dst_dir = os.path.join(src_dir, 'nonexistent_dir')
        open(os.path.join(src_dir, 'document.txt'), 'w').close()
        open(os.path.join(src_dir, 'notes.docx'), 'w').close()

        result = task_func(src_dir, dst_dir)
        assert result == dst_dir
        assert set(os.listdir(dst_dir)) == {'document.txt', 'notes.docx'}

def test_task_func_permissions():
    with tempfile.TemporaryDirectory() as src_dir, tempfile.TemporaryDirectory() as dst_dir:
        # Make source directory read-only
        os.chmod(src_dir, 0o444)
        open(os.path.join(src_dir, 'document.txt'), 'w').close()
        open(os.path.join(src_dir, 'notes.docx'), 'w').close()

        with pytest.raises(PermissionError):
            task_func(src_dir, dst_dir)