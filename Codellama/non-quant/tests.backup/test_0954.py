import pytest
from src_0954 import task_func
import numpy as np
import matplotlib.pyplot as plt
import os

def test_task_func():
    mystrings = ["apple", "banana", "orange"]
    folder_path = "test_folder"
    seed = 1234

    saved_plots = task_func(mystrings, folder_path, seed)

    assert len(saved_plots) == 3
    assert all(os.path.exists(os.path.join(folder_path, file_name)) for file_name in saved_plots)
    assert all(file_name.endswith(".png") for file_name in saved_plots)
    assert all(file_name.startswith(name.replace(" ", "_")) for name, file_name in zip(mystrings, saved_plots))

    for file_name in saved_plots:
        os.remove(os.path.join(folder_path, file_name))
    os.rmdir(folder_path)