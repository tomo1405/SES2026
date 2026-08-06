python
import os
from datetime import datetime
import pytest

def task_func(filepath: str) -> dict:
    try:
        size = os.path.getsize(filepath)
        mtime = os.path.getmtime(filepath)
        mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    except OSError as e:
        raise Exception(f"Error: {e}")

    return {'size': f"{size} bytes", 'last_modified': mtime}

def test_task_func_valid_filepath():
    filepath = 'test.txt'
    assert task_func(filepath) == {'size': '0 bytes', 'last_modified': '1970-01-01 00:00:00'}

def test_task_func_invalid_filepath():
    filepath = 'invalid.txt'
    with pytest.raises(Exception) as e:
        task_func(filepath)
    assert str(e.value) == "Error: [Errno 2] No such file or directory: 'invalid.txt'"