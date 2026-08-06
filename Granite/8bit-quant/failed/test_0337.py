import re
import os
import glob
from pathlib import Path
from unittest.mock import patch, call

def task_func(pattern, directory, extensions):
    matched_files = []
    for ext in extensions:
        files = glob.glob(os.path.join(directory, ext))
        for file in files:
            with open(file, 'r') as f:
                content = f.read().lower()
                if re.search(pattern.lower(), content):
                    matched_files.append(Path(file).resolve())
    return matched_files

def test_task_func():
    pattern = "example"
    directory = "/path/to/directory"
    extensions = [".txt", ".py"]
    with patch("glob.glob") as mock_glob, patch("pathlib.Path.resolve") as mock_resolve, patch("builtins.open", mock_open(read_data="Example content")):
        mock_glob.return_value = ["/path/to/directory/file1.txt", "/path/to/directory/file2.py"]
        mock_resolve.return_value = "/path/to/directory/file2.py"
        result = task_func(pattern, directory, extensions)
        assert result == ["/path/to/directory/file2.py"]
        assert mock_glob.call_args_list == [call(os.path.join(directory, "*.txt")), call(os.path.join(directory, "*.py"))]
        assert mock_resolve.call_args_list == [call()]