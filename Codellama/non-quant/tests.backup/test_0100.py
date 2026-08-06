import pytest
from src_0100 import task_func

def test_task_func():
    # Test that the function returns a matplotlib figure
    assert isinstance(task_func(), plt.Figure)

    # Test that the figure has the correct title
    assert task_func().suptitle == 'Iris Dataset Pair Plot'

    # Test that the figure has the correct number of axes
    assert len(task_func().axes) == 4

    # Test that the figure has the correct number of legend entries
    assert len(task_func().legend_.get_texts()) == 3

    # Test that the figure has the correct number of data points
    assert len(task_func().axes[0].lines[0].get_data()[0]) == 150

    # Test that the figure has the correct data range
    assert task_func().axes[0].get_xlim() == (0, 3)
    assert task_func().axes[0].get_ylim() == (0, 3)

    # Test that the figure has the correct data labels
    assert task_func().axes[0].get_xlabel() == 'sepal length (cm)'
    assert task_func().axes[0].get_ylabel() == 'sepal width (cm)'

    # Test that the figure has the correct legend labels
    assert task_func().legend_.get_texts()[0].get_text() == 'setosa'
    assert task_func().legend_.get_texts()[1].get_text() == 'versicolor'
    assert task_func().legend_.get_texts()[2].get_text() == 'virginica'