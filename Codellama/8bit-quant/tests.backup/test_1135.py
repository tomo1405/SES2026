import pytest
from src_1135 import task_func

def test_task_func_valid_input():
    source_dir = 'tests/data/source'
    target_dir = 'tests/data/target'
    prefix = '#Hash: '
    expected_files = [
        'tests/data/target/file1.txt',
        'tests/data/target/file2.txt',
        'tests/data/target/file3.txt',
    ]
    expected_hashes = [
        'd41d8cd98f00b204e9800998ecf8427e',
        'd41d8cd98f00b204e9800998ecf8427e',
        'd41d8cd98f00b204e9800998ecf8427e',
    ]

    new_files = task_func(source_dir, target_dir, prefix)

    assert new_files == expected_files
    for file_path in new_files:
        with open(file_path, 'r') as infile:
            content = infile.read()
        hash_object = hashlib.md5(content.encode())
        assert hash_object.hexdigest() in expected_hashes

def test_task_func_invalid_input():
    source_dir = 'tests/data/source'
    target_dir = 'tests/data/target'
    prefix = '#Hash: '

    with pytest.raises(FileNotFoundError):
        task_func(source_dir, target_dir, prefix)