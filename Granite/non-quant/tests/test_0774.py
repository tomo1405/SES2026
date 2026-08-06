import os
import re

from src_0774 import task_func

SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def test_task_func():
    # Mock the os.listdir() function to return a list of files in the source directory
    with mock.patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ['file-1.json', 'file-2.json', 'file-3.json']
        # Call the function to be tested
        task_func()
        # Check if the correct files were moved to the target directory
        expected_calls = [
            mock.call(os.path.join(SOURCE_DIR, 'file-1.json')),
            mock.call(os.path.join(SOURCE_DIR, 'file-2.json')),
            mock.call(os.path.join(SOURCE_DIR, 'file-3.json'))
        ]
        assert mock_move.call_args_list == expected_calls

def test_task_func_with_no_files():
    # Mock the os.listdir() function to return an empty list
    with mock.patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = []
        # Call the function to be tested
        task_func()
        # Check if no files were moved to the target directory
        assert mock_move.call_count == 0