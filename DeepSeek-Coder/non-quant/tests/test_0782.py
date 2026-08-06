import pytest
from src_0782 import task_func
import os
from datetime import datetime

def test_task_func_success():
    # Create a temporary file for testing
    with open('test_file.txt', 'w') as f:
        f.write('test')

    try:
        result = task_func('test_file.txt')
        assert result == {'size': '4 bytes', 'last_modified': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    finally:
        os.remove('test_file.txt')

def test_task_func_file_not_found():
    with pytest.raises(Exception):
        task_func('nonexistent_file.txt')