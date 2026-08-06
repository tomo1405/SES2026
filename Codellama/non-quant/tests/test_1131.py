import json
import os
import shutil

from src_1131 import task_func


def test_task_func():
    directory = 'test_directory'
    expected_hashes = {
        'test_directory/file1.txt': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
        'test_directory/file2.txt': '248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd41931fff4',
        'test_directory/subdir/file3.txt': '9ae16a3b2f0d471d7e2a40a01ee45b6729e95264b7753cf2f3a1ee0464f5d7ec'
    }

    # Create test directory and files
    os.makedirs(directory, exist_ok=True)
    for file_path, hash in expected_hashes.items():
        with open(file_path, 'w') as f:
            f.write('test data')

    # Run task function
    result = task_func(directory)

    # Check that the JSON file was created and contains the expected hashes
    assert os.path.isfile(result)
    with open(result, 'r') as f:
        actual_hashes = json.load(f)
    assert actual_hashes == expected_hashes

    # Clean up test directory
    shutil.rmtree(directory)