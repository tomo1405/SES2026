import pytest
from src_0827 import task_func
import os
import shutil
import tempfile

def test_task_func_nonexistent_source_dir():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/source/dir', '/target/dir')

def test_task_func_empty_source_dir():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        assert task_func(source_dir, target_dir) == 0

def test_task_func_no_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        open(os.path.join(source_dir, 'image.png'), 'w').close()
        open(os.path.join(source_dir, 'script.py'), 'w').close()
        assert task_func(source_dir, target_dir) == 0

def test_task_func_with_matching_files():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        open(os.path.join(source_dir, 'document.txt'), 'w').close()
        open(os.path.join(source_dir, 'report.doc'), 'w').close()
        open(os.path.join(source_dir, 'summary.docx'), 'w').close()
        assert task_func(source_dir, target_dir) == 3
        assert os.listdir(target_dir) == ['document.txt', 'report.doc', 'summary.docx']

def test_task_func_with_existing_target_dir():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        open(os.path.join(source_dir, 'file.txt'), 'w').close()
        open(os.path.join(target_dir, 'existing_file.txt'), 'w').close()
        assert task_func(source_dir, target_dir) == 1
        assert os.listdir(target_dir) == ['existing_file.txt', 'file.txt']

def test_task_func_custom_pattern():
    with tempfile.TemporaryDirectory() as source_dir, tempfile.TemporaryDirectory() as target_dir:
        open(os.path.join(source_dir, 'data.csv'), 'w').close()
        open(os.path.join(source_dir, 'notes.txt'), 'w').close()
        assert task_func(source_dir, target_dir, r'\b[A-Za-z0-9]+\.txt\b') == 1
        assert os.listdir(target_dir) == ['notes.txt']