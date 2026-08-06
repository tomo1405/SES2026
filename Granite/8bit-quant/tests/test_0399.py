import json
import os
import pytest

from src_0399 import task_func

def test_task_func():
    file_path = "test_file.json"
    with open(file_path, "w") as file:
        file.write("[{}]")

    assert task_func(file_path) == True

    with open(file_path, "w") as file:
        file.write("invalid json")

    assert task_func(file_path) == False

    os.remove(file_path)