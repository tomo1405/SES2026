import os
import re
import shutil
from src_0774 import task_func

SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def test_task_func():
    # Mock the os.listdir() function to return a list of files in the source directory
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = ['file1-1.json', 'file2-2.json', 'file3-3.json']
        # Call the function to be tested
        task_func()
        # Check if the files were moved to the target directory
        for filename in os.listdir(SOURCE_DIR):
            match = FILE_PATTERN.match(filename)
            if match is not None:
                prefix = match.group(1)
                new_filename = f'{prefix}.json'
                assert os.path.exists(os.path.join(TARGET_DIR, new_filename))

def test_task_func_no_files():
    # Mock the os.listdir() function to return an empty list
    with patch('os.listdir') as mock_listdir:
        mock_listdir.return_value = []
        # Call the function to be tested
        task_func()
        # Check if no files were moved to the target directory
        assert len(os.listdir(TARGET_DIR)) == 0