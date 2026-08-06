python
import numpy as np
import matplotlib.pyplot as plt
import os
import pytest

def task_func(mystrings, folder_path, seed=None):
    if seed is not None:
        np.random.seed(seed)

    saved_plots = []
    processed_names = set()

    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    for name in mystrings:
        if name in processed_names:
            continue
        data = np.random.rand(10)
        plt.bar(range(len(data)), data)
        plt.title(name)
        file_name = name.replace(" ", "_") + ".png"
        plt.savefig(os.path.join(folder_path, file_name))
        saved_plots.append(file_name)
        processed_names.add(name)

    return saved_plots

def test_task_func():
    mystrings = ["apple", "banana", "cherry", "apple", "banana"]
    folder_path = "plots"
    seed = 42

    saved_plots = task_func(mystrings, folder_path, seed)

    assert len(saved_plots) == 4
    assert "apple_1.png" in saved_plots
    assert "banana_1.png" in saved_plots
    assert "cherry.png" in saved_plots
    assert "apple_2.png" in saved_plots
    assert "banana_2.png" in saved_plots