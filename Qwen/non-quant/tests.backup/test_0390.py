import pytest
from src_0390 import task_func
import os
import shutil
import tempfile

def test_task_func_no_interesting_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files that do not match the pattern
        open(os.path.join(temp_dir, 'uninteresting.txt'), 'w').close()
        open(os.path.join(temp_dir, 'another_uninteresting.doc'), 'w').close()

        result = task_func(temp_dir)
        assert result == []
        assert not os.path.exists(os.path.join(temp_dir, 'Interesting Files'))

def test_task_func_with_interesting_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some files that match the pattern
        open(os.path.join(temp_dir, 'like_this.txt'), 'w').close()
        open(os.path.join(temp_dir, 'what_about_this.doc'), 'w').close()
        open(os.path.join(temp_dir, 'uninteresting.jpg'), 'w').close()

        result = task_func(temp_dir)
        assert sorted(result) == ['like_this.txt', 'what_about_this.doc']
        assert os.path.exists(os.path.join(temp_dir, 'Interesting Files'))
        assert os.path.exists(os.path.join(temp_dir, 'Interesting Files', 'like_this.txt'))
        assert os.path.exists(os.path.join(temp_dir, 'Interesting Files', 'what_about_this.doc'))
        assert not os.path.exists(os.path.join(temp_dir, 'like_this.txt'))
        assert not os.path.exists(os.path.join(temp_dir, 'what_about_this.doc'))

def test_task_func_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == []
        assert not os.path.exists(os.path.join(temp_dir, 'Interesting Files'))

def test_task_func_case_insensitivity():
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with different cases
        open(os.path.join(temp_dir, 'LIKE_this.txt'), 'w').close()
        open(os.path.join(temp_dir, 'WHAT_about_this.doc'), 'w').close()

        result = task_func(temp_dir)
        assert sorted(result) == ['LIKE_this.txt', 'WHAT_about_this.doc']
        assert os.path.exists(os.path.join(temp_dir, 'Interesting Files'))
        assert os.path.exists(os.path.join(temp_dir, 'Interesting Files', 'LIKE_this.txt'))
        assert os.path.exists(os.path.join(temp_dir, 'Interesting Files', 'WHAT_about_this.doc'))
        assert not os.path.exists(os.path.join(temp_dir, 'LIKE_this.txt'))
        assert not os.path.exists(os.path.join(temp_dir, 'WHAT_about_this.doc'))