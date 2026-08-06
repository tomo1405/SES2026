import pytest
from src_0205 import task_func
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def test_task_func():
    # Test with a simple list
    L = [1, 2, 3, 4, 5]
    result = task_func(L)
    assert result['mean'] == np.mean(L)
    assert result['median'] == np.median(L)
    assert result['mode'] == Counter(L).most_common(1)[0][0]
    assert np.isclose(result['std_dev'], np.std(L))
    assert isinstance(result['plot'], plt.Axes)

    # Test with a list having multiple modes
    L = [1, 1, 2, 2, 3]
    result = task_func(L)
    assert result['mode'] == 1  # Mode should be the first one in case of a tie

    # Test with a list containing negative numbers
    L = [-5, -3, -1, 1, 3, 5]
    result = task_func(L)
    assert result['mean'] == np.mean(L)
    assert result['median'] == np.median(L)
    assert result['mode'] == Counter(L).most_common(1)[0][0]
    assert np.isclose(result['std_dev'], np.std(L))

    # Test with a list containing a single element
    L = [42]
    result = task_func(L)
    assert result['mean'] == 42
    assert result['median'] == 42
    assert result['mode'] == 42
    assert result['std_dev'] == 0
    assert isinstance(result['plot'], plt.Axes)

    # Test with an empty list (should raise an error)
    with pytest.raises(np.AxisError):
        task_func([])

    # Test with a list containing NaN values (should raise an error)
    L = [1, 2, np.nan, 4, 5]
    with pytest.raises(ValueError):
        task_func(L)

    # Test with a list containing Inf values (should raise an error)
    L = [1, 2, np.inf, 4, 5]
    with pytest.raises(ValueError):
        task_func(L)