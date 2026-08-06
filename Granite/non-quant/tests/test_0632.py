import csv
import os
import pytest
from src_0632 import task_func

def test_task_func():
    df = ...  # Mock DataFrame
    filename = 'test_file.csv'
    output_dir = '/tmp/output'  # Mock output directory

    file_path = task_func(df, filename, output_dir)

    assert file_path.startswith(output_dir)
    assert os.path.exists(file_path)
    assert file_path.endswith(filename)