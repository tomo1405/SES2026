import os

import pandas as pd
from src_0603 import task_func


def test_task_func_output_file_exists(tmpdir):
    file_path = str(tmpdir / 'test_output.csv')
    output_dir = str(tmpdir / 'test_output_dir')
    task_func(file_path, output_dir=output_dir)
    assert os.path.exists(file_path)

def test_task_func_output_directory_created(tmpdir):
    file_path = str(tmpdir / 'test_output.csv')
    output_dir = str(tmpdir / 'test_output_dir')
    task_func(file_path, output_dir=output_dir)
    assert os.path.exists(output_dir)

def test_task_func_output_file_content(tmpdir):
    file_path = str(tmpdir / 'test_output.csv')
    output_dir = str(tmpdir / 'test_output_dir')
    task_func(file_path, output_dir=output_dir)
    df = pd.read_csv(file_path, sep='\t', header=None)
    assert df.shape == (10, 10)
    assert all(df.values.flatten() in LETTERS for letter in LETTERS)