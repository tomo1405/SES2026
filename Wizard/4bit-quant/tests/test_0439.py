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
    # Test case 1: Test with valid input
    numbers = [1, 2, 3, 4, 5]
    file_path = "test.pkl"
    expected_fig = plt.figure()
    expected_fig.plot(numbers)
    actual_fig = task_func(numbers, file_path)
    assert actual_fig == expected_fig

    # Test case 2: Test with invalid input
    numbers = [1, 2, "3", 4, 5]
    with pytest.raises(TypeError):
        task_func(numbers)

    # Test case 3: Test with file_path as None
    numbers = [1, 2, 3, 4, 5]
    file_path = None
    expected_fig = plt.figure()
    expected_fig.plot(numbers)
    actual_fig = task_func(numbers, file_path)
    assert actual_fig == expected_fig

    # Test case 4: Test with file_path as empty string
    numbers = [1, 2, 3, 4, 5]
    file_path = ""
    expected_fig = plt.figure()
    expected_fig.plot(numbers)
    actual_fig = task_func(numbers, file_path)
    assert actual_fig == expected_fig

    # Test case 5: Test with file_path as valid string
    numbers = [1, 2, 3, 4, 5]
    file_path = "test.pkl"
    expected_fig = plt.figure()
    expected_fig.plot(numbers)
    actual_fig = task_func(numbers, file_path)
    assert actual_fig == expected_fig

    # Test case 6: Test with file_path as invalid string
    numbers = [1, 2, 3, 4, 5]
    file_path = "test.png"
    with pytest.raises(FileNotFoundError):
        task_func(numbers, file_path)

    # Test case 7: Test with file_path as valid string but file not found
    numbers = [1, 2, 3, 4, 5]
    file_path = "test.pkl"
    os.remove(file_path)
    with pytest.raises(FileNotFoundError):
        task_func(numbers, file_path)