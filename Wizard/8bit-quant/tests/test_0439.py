python
import pickle
import os
import matplotlib.pyplot as plt
import pytest

def task_func(numbers, file_path="save.pkl"):

    if not isinstance(numbers, list) or not all(
        isinstance(item, (int, float)) for item in numbers
    ):
        raise TypeError("Expect list of numbers.")

    fig = plt.figure()
    plt.plot(numbers)

    with open(file_path, "wb") as file:
        pickle.dump(fig, file)

    with open(file_path, "rb") as file:
        loaded_fig = pickle.load(file)

    os.remove(file_path)

    return loaded_fig

def test_task_func():
    # Test case 1: Valid input
    numbers = [1, 2, 3, 4, 5]
    file_path = "test.pkl"
    expected_fig = plt.figure()
    expected_fig.plot(numbers)
    expected_fig.savefig(file_path)
    loaded_fig = task_func(numbers, file_path)
    assert loaded_fig == expected_fig
    os.remove(file_path)

    # Test case 2: Invalid input (not a list of numbers)
    numbers = [1, 2, 3, "4", 5]
    with pytest.raises(TypeError):
        task_func(numbers)

    # Test case 3: Invalid input (empty list)
    numbers = []
    with pytest.raises(TypeError):
        task_func(numbers)

    # Test case 4: Invalid input (file path is not a string)
    numbers = [1, 2, 3, 4, 5]
    file_path = 123
    with pytest.raises(TypeError):
        task_func(numbers, file_path)

    # Test case 5: Invalid input (file path is empty)
    numbers = [1, 2, 3, 4, 5]
    file_path = ""
    with pytest.raises(TypeError):
        task_func(numbers, file_path)