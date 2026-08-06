python
import pytest
from src_0954 import task_func

def test_task_func():
    mystrings = ["apple", "banana", "cherry", "apple", "banana"]
    folder_path = "plots"
    seed = 42

    saved_plots = task_func(mystrings, folder_path, seed)

    assert len(saved_plots) == 2
    assert "apple_1.png" in saved_plots
    assert "banana_2.png" in saved_plots