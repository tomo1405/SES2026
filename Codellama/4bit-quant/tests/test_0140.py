import pytest
from src_0140 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Test 1: Input is not a DataFrame
    with pytest.raises(ValueError):
        task_func(1)

    # Test 2: Input is an empty DataFrame
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test 3: Input has no numeric columns
    df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['d', 'e', 'f']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test 4: Input has numeric columns
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    axes = task_func(df)
    assert isinstance(axes, list)
    assert len(axes) == 2
    for ax in axes:
        assert isinstance(ax, plt.Axes)
        assert ax.get_title() in ['A', 'B']
        assert ax.get_xlabel() == 'Value'
        assert ax.get_ylabel() == 'Frequency'

if __name__ == '__main__':
    pytest.main()