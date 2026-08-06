import pytest
from src_0954 import task_func
import os
import numpy as np
import matplotlib.pyplot as plt

@pytest.fixture
def setup():
    return "test_folder"

def test_task_func(setup):
    mystrings = ["test1", "test2"]
    folder_path = setup
    result = task_func(mystrings=mystrings, folder_path=folder_path)
    assert os.path.exists(folder_path)
    assert len(os.listdir(folder_path)) > 0
    assert len(os.listdir(folder_path)) == len(mystrings)

def test_task_func_with_seed(setup):
    mystrings = ["test1", "test2"]
    folder_path = setup
    result = task_func(mystrings=mystrings, folder_path=folder_path, seed=42)
    first_plot = os.listdir(folder_path)[0]
    second_plot = os.listdir(folder_path)[1]
    assert first_plot != second_plot