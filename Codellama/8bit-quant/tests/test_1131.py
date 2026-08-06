import json
from unittest.mock import patch

from src_1131 import task_func


def test_task_func():
    directory = 'path/to/directory'
    expected_hashes = {
        'path/to/directory/file1.txt': 'hash1',
        'path/to/directory/file2.txt': 'hash2',
        'path/to/directory/file3.txt': 'hash3'
    }
    expected_json_file = 'path/to/directory/hashes.json'

    # Mock the os.walk function to return the expected files and directories
    with patch('os.walk') as mock_walk:
        mock_walk.return_value = [
            (directory, [], ['file1.txt', 'file2.txt', 'file3.txt']),
            (directory + '/file1.txt', [], []),
            (directory + '/file2.txt', [], []),
            (directory + '/file3.txt', [], [])
        ]

        # Mock the open function to return a mock file object
        with patch('builtins.open', mock_open()) as mock_file:
            # Mock the file object to return the expected bytes
            mock_file.return_value.read.return_value = b'file contents'

            # Call the task_func function with the mocked directory
            result = task_func(directory)

            # Assert that the result is the expected JSON file
            assert result == expected_json_file

            # Assert that the JSON file contains the expected hashes
            with open(expected_json_file, 'r') as f:
                actual_hashes = json.load(f)
                assert actual_hashes == expected_hashes