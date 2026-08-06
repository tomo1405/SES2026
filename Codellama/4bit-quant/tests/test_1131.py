import pytest
from src_1131 import task_func

def test_task_func():
    directory = 'path/to/directory'
    expected_hash_dict = {
        'path/to/directory/file1': 'hash1',
        'path/to/directory/file2': 'hash2',
        'path/to/directory/file3': 'hash3'
    }
    expected_json_file = 'path/to/directory/hashes.json'

    with pytest.raises(ValueError):
        task_func(directory)

    assert os.path.exists(expected_json_file)
    with open(expected_json_file, 'r') as f:
        actual_hash_dict = json.load(f)
        assert actual_hash_dict == expected_hash_dict