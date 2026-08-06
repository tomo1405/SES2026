import pytest
from src_0439 import task_func

def test_task_func():
    numbers = [1, 2, 3, 4, 5]
    file_path = "save.pkl"

    with pytest.raises(TypeError):
        task_func(numbers, file_path)

    numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    with pytest.raises(TypeError):
        task_func(numbers, file_path)

    numbers = [1, 2, 3, 4, 5]
    loaded_fig = task_func(numbers, file_path)
    assert isinstance(loaded_fig, matplotlib.figure.Figure)

    os.remove(file_path)