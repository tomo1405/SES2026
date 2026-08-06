import pytest
from src_0709 import task_func
import json
import csv
import os
import base64

def test_task_func():
    raw_string = "eyJzdHJpbmciOiAiSGVsbG8gV29ybGQifQ=="
    filename = "test_file"
    output_dir = "test_output"

    file_path = task_func(raw_string, filename, output_dir)

    assert file_path == os.path.join(output_dir, f'{filename}.csv')

    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        data = {row[0]: row[1] for row in reader}

    assert data == {'string': 'Hello World'}