import numpy as np
import matplotlib.pyplot as plt
import os
import pytest
from src_0954 import task_func

def test_task_func():
    mystrings = ["apple", "banana", "cherry"]
    folder_path = "/tmp/plots"
    seed = 42
    saved_plots = task_func(mystrings, folder_path, seed)
    assert len(saved_plots) == len(mystrings)
    for plot_file in saved_plots:
        assert plot_file.endswith(".png")
        assert os.path.exists(os.path.join(folder_path, plot_file))