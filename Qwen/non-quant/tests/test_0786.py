import os
from unittest.mock import call, patch

from src_0786 import task_func

# Constants
ARCHIVE_DIR = '/tmp/archive'

def test_task_func_no_files_found():
    with patch('glob.glob', return_value=[]):
        result = task_func('*.txt')
        assert result == "No files found matching the pattern."

def test_task_func_files_found():
    mock_glob = ['file1.txt', 'file2.txt']
    with patch('glob.glob', return_value=mock_glob), \
         patch('subprocess.run') as mock_subprocess, \
         patch('os.path.exists', side_effect=[False, False]), \
         patch('os.makedirs'), \
         patch('os.remove'):
        
        result = task_func('*.txt')
        
        expected_archive_file = os.path.join(ARCHIVE_DIR, 'archive.tar.gz')
        assert result == expected_archive_file
        
        mock_subprocess.assert_called_once_with(['tar', '-czf', expected_archive_file] + mock_glob)
        mock_os_remove_calls = [call('file1.txt'), call('file2.txt')]
        mock_os_remove.assert_has_calls(mock_os_remove_calls)

def test_task_func_archive_exists():
    mock_glob = ['file1.txt', 'file2.txt']
    with patch('glob.glob', return_value=mock_glob), \
         patch('subprocess.run') as mock_subprocess, \
         patch('os.path.exists', side_effect=[False, True, False]), \
         patch('os.makedirs'), \
         patch('os.remove'):
        
        result = task_func('*.txt')
        
        expected_archive_file = os.path.join(ARCHIVE_DIR, 'archive_1.tar.gz')
        assert result == expected_archive_file
        
        mock_subprocess.assert_called_once_with(['tar', '-czf', expected_archive_file] + mock_glob)
        mock_os_remove_calls = [call('file1.txt'), call('file2.txt')]
        mock_os_remove.assert_has_calls(mock_os_remove_calls)

def test_task_func_directory_creation():
    with patch('glob.glob', return_value=['file1.txt']), \
         patch('subprocess.run'), \
         patch('os.path.exists', return_value=False), \
         patch('os.makedirs') as mock_makedirs, \
         patch('os.remove'):
        
        task_func('*.txt')
        
        mock_makedirs.assert_called_once_with(ARCHIVE_DIR)