import matplotlib.pyplot as plt
import pytest
from src_0125 import task_func


def test_task_func():
    # Test that the function raises a TypeError if the input is not a list
    with pytest.raises(TypeError):
        task_func(123)

    # Test that the function raises a ValueError if the input list contains non-numeric elements
    with pytest.raises(ValueError):
        task_func(['a', 'b', 'c'])

    # Test that the function returns a tuple with two elements
    result = task_func([1, 2, 3])
    assert len(result) == 2

    # Test that the first element of the tuple is a float
    assert isinstance(result[0], float)

    # Test that the second element of the tuple is a matplotlib.axes.Axes object
    assert isinstance(result[1], plt.Axes)

    # Test that the function appends 12 to the input list
    my_list = [1, 2, 3]
    task_func(my_list)
    assert my_list[-1] == 12

    # Test that the function returns the correct histogram
    result = task_func([1, 2, 3])
    assert result[1].get_title() == 'Histogram of Random Numbers'
    assert result[1].get_xlabel() == 'Number'
    assert result[1].get_ylabel() == 'Frequency'