import pytest
from src_0007 import task_func
import os
import tempfile
import re

def create_temp_log_files(tmpdir, files):
    for file_name in files:
        tmpdir.join(file_name).write('')

def test_task_func_no_matching_files(tmpdir):
    pattern = r'^nonexistent.*'
    create_temp_log_files(tmpdir, ['file1.log', 'file2.log'])
    result = task_func(pattern, str(tmpdir))
    assert result is None

def test_task_func_single_matching_file(tmpdir):
    pattern = r'^file1.*'
    create_temp_log_files(tmpdir, ['file1.log', 'file2.log'])
    result = task_func(pattern, str(tmpdir))
    assert result == str(tmpdir.join('file1.log'))

def test_task_func_multiple_matching_files(tmpdir):
    pattern = r'^file.*'
    create_temp_log_files(tmpdir, ['file1.log', 'file2.log', 'file3.log'])
    # Touch files to set different modification times
    with open(str(tmpdir.join('file1.log')), 'a') as f:
        pass
    with open(str(tmpdir.join('file3.log')), 'a') as f:
        pass
    result = task_func(pattern, str(tmpdir))
    assert result == str(tmpdir.join('file3.log'))

def test_task_func_empty_pattern(tmpdir):
    pattern = r''
    create_temp_log_files(tmpdir, ['file1.log', 'file2.log'])
    result = task_func(pattern, str(tmpdir))
    assert result is None

def test_task_func_nonexistent_directory():
    pattern = r'^.*'
    with pytest.raises(FileNotFoundError):
        task_func(pattern, '/nonexistent/directory')