import os
import hashlib
import json
from pathlib import Path
from unittest.mock import patch, call

import pytest

from src_1131 import task_func

def test_task_func():
    directory = "/path/to/directory"
    with patch("os.walk") as mock_walk, patch("pathlib.Path.open") as mock_open, patch("json.dump") as mock_json_dump:
        mock_walk.return_value = [
            ("/path/to/directory", ["dir1", "dir2"], ["file1.txt", "file2.txt"]),
            ("/path/to/directory/dir1", [], ["file3.txt"]),
            ("/path/to/directory/dir2", [], ["file4.txt", "file5.txt"])
        ]
        mock_open.return_value.__enter__.return_value = mock_open.return_value
        mock_json_dump.return_value = None

        result = task_func(directory)

        mock_walk.assert_called_once_with(directory)
        mock_open.assert_has_calls([
            call().__enter__(),
            call().__exit__(None, None, None),
            call().__enter__(),
            call().__exit__(None, None, None),
            call().__enter__(),
            call().__exit__(None, None, None),
            call().__enter__(),
            call().__exit__(None, None, None)
        ])
        mock_json_dump.assert_called_once_with(
            {
                "/path/to/directory/file1.txt": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
                "/path/to/directory/file2.txt": "45c48bc8000d26546b08358aa7fe30229e936b46c30d3f0ae9b609d45f97b92e",
                "/path/to/directory/dir1/file3.txt": "45c48bc8000d26546b08358aa7fe30229e936b46c30d3f0ae9b609d45f97b92e",
                "/path/to/directory/dir2/file4.txt": "45c48bc8000d26546b08358aa7fe30229e936b46c30d3f0ae9b609d45f97b92e",
                "/path/to/directory/dir2/file5.txt": "45c48bc8000d26546b08358aa7fe30229e936b46c30d3f0ae9b609d45f97b92e"
            },
            mock_open.return_value,
            indent=4
        )
        assert result == "/path/to/directory/hashes.json"