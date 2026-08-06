import os

import pytest
from src_0603 import task_func


def test_task_func_with_valid_input():
    file_path = 'output/test_matrix.txt'
    task_func(file_path)
    assert os.path.exists(file_path)
    matrix = pd.read_csv(file_path, sep='\t', header=None)
    assert matrix.shape == (10, 10)
    assert matrix.iloc[0, 0] in list('abcdefghijklmnopqrstuvwxyz')
    os.remove(file_path)

def test_task_func_with_invalid_input():
    with pytest.raises(TypeError):
        task_func(123)
    with pytest.raises(TypeError):
        task_func('output/test_matrix.txt', 123)

def test_task_func_with_nonexistent_output_dir():
    file_path = 'output/test_matrix.txt'
    if os.path.exists('output'):
        os.rmdir('output')
    task_func(file_path)
    assert os.path.exists(file_path)
    os.remove(file_path)