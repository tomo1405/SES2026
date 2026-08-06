import re
import os
from pathlib import Path
import glob
import pytest

def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
    FILE_PATTERN = '*.txt'
    match_dict = {}
    file_paths = glob.glob(os.path.join(directory_path, FILE_PATTERN))
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            matches = re.findall(regex_pattern, content)
            match_dict[Path(file_path).name] = matches

    return match_dict

def test_task_func():
    directory_path = '/path/to/directory'
    regex_pattern = r'\\(.+?\\)|\\w'
    expected_output = {'file1.txt': ['match1', 'match2'], 'file2.txt': ['match3', 'match4']}
    
    actual_output = task_func(directory_path, regex_pattern)
    
    assert actual_output == expected_output