import pytest
from src_0439 import task_func

def test_task_func_valid_input():
    numbers = [1, 2, 3, 4, 5]
    file_path = "save.pkl"
    expected_fig = plt.figure()
    plt.plot(numbers)

    with open(file_path, "wb") as file:
        pickle.dump(expected_fig, file)

    loaded_fig = task_func(numbers, file_path)

    assert loaded_fig == expected_fig

def test_task_func_invalid_input():
    numbers = [1, 2, 3, 4, "a"]
    file_path = "save.pkl"

    with pytest.raises(TypeError):
        task_func(numbers, file_path)

def test_task_func_file_not_found():
    numbers = [1, 2, 3, 4, 5]
    file_path = "save.pkl"

    with pytest.raises(FileNotFoundError):
        task_func(numbers, file_path)