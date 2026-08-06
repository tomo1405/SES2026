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

def test_task_func():
    filepath = 'test.txt'
    with open(filepath, 'w') as f:
        f.write('test')

    result = task_func(filepath)
    assert result['size'] == '4 bytes'
    assert result['last_modified'] == datetime.fromtimestamp(os.path.getmtime(filepath)).strftime('%Y-%m-%d %H:%M:%S')

    os.remove(filepath)

    with pytest.raises(Exception):
        task_func('non_existent_file.txt')