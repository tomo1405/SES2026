import re
import json
import os
from src_0330 import task_func

def test_task_func():
    file_path = 'path/to/file.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
        text = ' '.join(data.values())
    regex_pattern = r'\(.+?\)|\w'
    matches = re.findall(regex_pattern, text)
    expected_match_dict = {os.path.basename(file_path): matches}
    actual_match_dict = task_func(file_path, regex_pattern)
    assert actual_match_dict == expected_match_dict

def test_task_func_with_custom_regex_pattern():
    file_path = 'path/to/file.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
        text = ' '.join(data.values())
    regex_pattern = r'\d+'
    matches = re.findall(regex_pattern, text)
    expected_match_dict = {os.path.basename(file_path): matches}
    actual_match_dict = task_func(file_path, regex_pattern)
    assert actual_match_dict == expected_match_dict