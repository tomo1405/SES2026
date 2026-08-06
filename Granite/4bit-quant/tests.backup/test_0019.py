import pytest
from src_0019 import task_func
import os
import subprocess
import csv
import glob
import random

def test_task_func_file_exists():
    file = "test.csv"
    with open(file, "w") as f:
        pass
    split_files = task_func(file)
    assert len(split_files) > 0
    os.remove(file)
    for split_file in split_files:
        os.remove(split_file)

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
    os.remove(file)

def test_task_func_exception():
    file = "test.csv"
    with open(file, "w") as f:
        pass
    with pytest.raises(Exception):
        subprocess.call(['split', '-n', '5', '-d', file, 'split_'])
    os.remove(file)

def test_task_func_shuffle():
    file = "test.csv"
    with open(file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["a", "b", "c"])
        writer.writerow(["1", "2", "3"])
        writer.writerow(["4", "5", "6"])
    split_files = task_func(file)
    with open(split_files[0], "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert len(rows) == 3
    os.remove(file)
    for split_file in split_files:
        os.remove(split_file)