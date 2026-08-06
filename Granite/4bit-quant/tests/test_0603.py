import os

import pandas as pd
import pytest
from src_0603 import task_func

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def test_task_func_with_valid_input():
    file_path = 'test_file.txt'
    task_func(file_path)
    assert os.path.exists(file_path)
    matrix = pd.read_csv(file_path, sep='\t', header=None)
    assert matrix.shape == (10, 10)
    assert matrix.iloc[0, 0] in LETTERS
    assert os.path.exists(OUTPUT_DIR)
    os.remove(file_path)
    os.rmdir(OUTPUT_DIR)

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)

    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.txt')