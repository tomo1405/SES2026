python
import pandas as pd
import pytest
from src_1063 import task_func

def test_task_func():
    # Test for empty array
    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

    # Test for non-empty array
    arr = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
    ax = task_func(arr)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Time Series of Row Sums"