import pytest
from src_0261 import task_func

def test_task_func():
    directory = 'path/to/directory'
    files = ['file1.json', 'file2.json', 'file3.json']
    updated_files = 0

    for file in files:
        with open(file, 'r+') as f:
            data = json.load(f)
            if KEY not in data:
                data[KEY] = VALUE
                f.seek(0)
                f.truncate()
                json.dump(data, f)
                updated_files += 1

    assert updated_files == 3

def test_task_func_with_existing_key():
    directory = 'path/to/directory'
    files = ['file1.json', 'file2.json', 'file3.json']
    updated_files = 0

    for file in files:
        with open(file, 'r+') as f:
            data = json.load(f)
            data[KEY] = VALUE
            f.seek(0)
            f.truncate()
            json.dump(data, f)
            updated_files += 1

    assert updated_files == 0