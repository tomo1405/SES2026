import pytest
from src_0603 import task_func
import os
import pandas as pd

def test_task_func_output_file_exists(tmpdir):
    file_path = tmpdir.join("test_output.csv")
    task_func(str(file_path))
    assert os.path.exists(file_path)

def test_task_func_file_content(tmpdir):
    file_path = tmpdir.join("test_output.csv")
    task_func(str(file_path))
    df = pd.read_csv(file_path, sep='\t', header=None)
    assert df.shape == (10, 10)
    assert all(df.applymap(lambda x: x in LETTERS).values.flatten())

def test_task_func_output_directory_creation(tmpdir):
    output_dir = tmpdir.join("custom_output")
    file_path = os.path.join(output_dir, "test_output.csv")
    task_func(file_path, output_dir=str(output_dir))
    assert os.path.exists(output_dir)
    assert os.path.exists(file_path)

def test_task_func_no_header_index(tmpdir):
    file_path = tmpdir.join("test_output.csv")
    task_func(str(file_path))
    with open(file_path) as f:
        lines = f.readlines()
    assert len(lines[0].strip().split('\t')) == 10
    assert not lines[0].startswith('#')