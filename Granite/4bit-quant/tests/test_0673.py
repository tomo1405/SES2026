import csv
import os

import pytest
from src_0673 import task_func


def test_task_func():
    filename = "example.csv"
    with open(filename, "w") as file:
        file.write("1,2,3\n4,5,6\n7,8,9")
    output = task_func(filename)
    with open(output, "r") as file:
        rows = list(csv.reader(file))
    assert rows == [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
    os.remove(filename)

def test_task_func_with_exception():
    filename = "nonexistent.csv"
    with pytest.raises(FileNotFoundError):
        task_func(filename)