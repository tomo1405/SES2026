import pytest
from src_0019 import task_func
import subprocess
import csv
import glob
import random
import os

def test_task_func_file_exists():
    file = "test.csv"
    with open(file, "w") as f:
        pass
    split_files = task_func(file)
    assert len(split_files) > 0
    for split_file in split_files:
        assert os.path.exists(split_file)

def test_task_func_file_not_exists():
    file = "test.csv"
    split_files = task_func(file)
    assert len(split_files) == 0

def test_task_func_not_csv():
    file = "test.txt"
    with open(file, "w") as f:
        pass
    split_files = task_func(file)
    assert len(split_files) == 0

def test_task_func_exception():
    file = "test.csv"
    with open(file, "w") as f:
        pass
    with pytest.raises(Exception):
        subprocess.call(['split', '-n', '5', '-d', file, 'split_'], stdout=subprocess.DEVNULL)