import pytest
from src_0328 import task_func

def test_task_func():
    file_path = 'path/to/your/file.csv'
    regex_pattern = r'\(.+?\)|\w+|[\W_]+'
    expected_output = {'apple': 1, 'banana': 2, 'orange': 3}
    
    actual_output = task_func(file_path, regex_pattern)
    
    assert actual_output == expected_output