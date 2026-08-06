import os
from tempfile import NamedTemporaryFile

import matplotlib.pyplot as plt
import pytest
from src_0439 import task_func


def test_task_func_valid_input():
    numbers = [1, 2, 3, 4, 5]
    loaded_fig = task_func(numbers)
    assert isinstance(loaded_fig, plt.Figure)

def test_task_func_invalid_input():
    with pytest.raises(TypeError):
        task_func("not a list")

def test_task_func_file_path():
    numbers = [1, 2, 3, 4, 5]
    with NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name
        loaded_fig = task_func(numbers, file_path)
        assert loaded_fig is not None
        assert os.path.exists(file_path)
    os.remove(file_path)