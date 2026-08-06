import matplotlib.pyplot as plt
from src_0100 import task_func


def test_task_func():
    # Test that the function returns a figure object
    assert isinstance(task_func(), plt.Figure)

    # Test that the figure has the correct title
    assert task_func().suptitle == 'Iris Dataset Pair Plot'

    # Test that the figure has the correct font family
    assert task_func().rcParams['font.family'] == 'Arial'

    # Test that the figure has the correct number of axes
    assert len(task_func().axes) == 4

    # Test that the figure has the correct number of lines
    assert len(task_func().lines) == 15

    # Test that the figure has the correct number of patches
    assert len(task_func().patches) == 15

    # Test that the figure has the correct number of texts
    assert len(task_func().texts) == 15