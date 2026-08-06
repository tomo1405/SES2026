import os
import pickle

import matplotlib.pyplot as plt
import pytest
from src_0439 import task_func


def test_task_func_valid_input():
    numbers = [1, 2, 3, 4, 5]
    file_path = "save.pkl"
    expected_fig = plt.figure()
    plt.plot(numbers)

    with open(file_path, "wb") as file:
        pickle.dump(expected_fig, file)

    with open(file_path, "rb") as file:
        loaded_fig = pickle.load(file)

    os.remove(file_path)

    assert task_func(numbers, file_path) == loaded_fig

def test_task_func_invalid_input():
    numbers = [1, 2, 3, 4, 5]
    file_path = "save.pkl"
    expected_fig = plt.figure()
    plt.plot(numbers)

    with open(file_path, "wb") as file:
        pickle.dump(expected_fig, file)

    with open(file_path, "rb") as file:
        loaded_fig = pickle.load(file)

    os.remove(file_path)

    with pytest.raises(TypeError):
        task_func("invalid input", file_path)