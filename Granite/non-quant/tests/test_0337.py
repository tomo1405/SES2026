import re
import os
import glob
from pathlib import Path
import pytest

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
    matched_files = task_func(pattern, directory, extensions)
    assert len(matched_files) > 0