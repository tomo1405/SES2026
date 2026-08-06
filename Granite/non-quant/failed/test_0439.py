import pickle
import os
import matplotlib.pyplot as plt
from unittest.mock import patch

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
    numbers = [1, 2, 3, 4, 5]
    file_path = "save.pkl"

    with patch("matplotlib.pyplot.figure") as mock_figure:
        with patch("pickle.dump") as mock_dump:
            with patch("pickle.load") as mock_load:
                with patch("os.remove") as mock_remove:
                    result = task_func(numbers, file_path)
                    mock_figure.assert_called_once()
                    mock_dump.assert_called_once()
                    mock_load.assert_called_once()
                    mock_remove.assert_called_once_with(file_path)
                    assert result == mock_load.return_value

def test_task_func_invalid_input():
    numbers = "not a list"
    file_path = "save.pkl"
    with pytest.raises(TypeError) as excinfo:
        task_func(numbers, file_path)
    assert "Expect list of numbers." in str(excinfo.value)