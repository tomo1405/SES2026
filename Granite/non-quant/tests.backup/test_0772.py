import re
import os
from pathlib import Path
import csv
from src_0772 import task_func

def test_task_func():
    directory = '/path/to/directory'
    pattern = r'^(.*?)-\d+\.csv$'
    new_files = task_func(directory, pattern)
    assert isinstance(new_files, list)
    for filename in new_files:
        assert filename.endswith('.csv')
        assert os.path.exists(Path(directory) / filename)