import pytest
from src_0100 import task_func

def test_task_func():
    # Test that the function returns a matplotlib figure
    assert isinstance(task_func(), plt.Figure)

    # Test that the figure has the correct title
    assert task_func().suptitle == 'Iris Dataset Pair Plot'

    # Test that the figure has the correct font family
    assert task_func().rcParams['font.family'] == 'Arial'

    # Test that the figure has the correct number of axes
    assert len(task_func().axes) == 4

    # Test that the figure has the correct number of legend entries
    assert len(task_func().legend.get_texts()) == 3

    # Test that the figure has the correct number of data points
    assert len(task_func().axes[0].lines[0].get_data()[0]) == 150
    assert len(task_func().axes[1].lines[0].get_data()[0]) == 150
    assert len(task_func().axes[2].lines[0].get_data()[0]) == 150
    assert len(task_func().axes[3].lines[0].get_data()[0]) == 150