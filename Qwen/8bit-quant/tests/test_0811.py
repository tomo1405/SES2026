import pytest
from src_0811 import task_func
import os
import subprocess
from unittest.mock import patch, mock_open

# Mocking os.walk to simulate directory structure
@patch('os.walk')
def test_task_func(mock_walk):
    # Mock directory structure
    mock_walk.return_value = [
        ('/root', ['dir1'], ['file1.txt', 'file2.exe']),
        ('/root/dir1', [], ['file3.exe', 'file4.txt'])
    ]
    
    # Mock subprocess.run to simulate execution of files
    with patch.object(subprocess, 'run') as mock_run:
        mock_run.return_value = subprocess.CompletedProcess(args=[], returncode=0, stdout=b'Output of file2.exe')
        
        # Test case where files are executed
        results = task_func('/root', r'\.exe$', True)
        assert results == ['Output of file2.exe']
        
        # Test case where files are not executed
        results = task_func('/root', r'\.exe$', False)
        assert results == ['/root/file2.exe', '/root/dir1/file3.exe']

# Test case for non-existent directory
def test_task_func_non_existent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/non_existent_dir', r'\.exe$')

# Test case for no matching files
@patch('os.walk')
def test_task_func_no_matching_files(mock_walk):
    mock_walk.return_value = [
        ('/root', ['dir1'], ['file1.txt', 'file2.txt']),
        ('/root/dir1', [], ['file3.txt', 'file4.txt'])
    ]
    
    results = task_func('/root', r'\.exe$', True)
    assert results == []

# Test case for empty directory
@patch('os.walk')
def test_task_func_empty_directory(mock_walk):
    mock_walk.return_value = [
        ('/root', [], [])
    ]
    
    results = task_func('/root', r'\.exe$', True)
    assert results == []

# Test case for different pattern
@patch('os.walk')
def test_task_func_different_pattern(mock_walk):
    mock_walk.return_value = [
        ('/root', ['dir1'], ['file1.txt', 'file2.doc']),
        ('/root/dir1', [], ['file3.doc', 'file4.txt'])
    ]
    
    results = task_func('/root', r'\.doc$', False)
    assert results == ['/root/file2.doc', '/root/dir1/file3.doc']