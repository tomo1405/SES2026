python
import pytest
from src_0045 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df, ax = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert ax.get_xlabel() == 'Scaled Values'
    assert ax.get_ylabel() == 'Features'
    assert ax.get_title() == 'Boxplot of Scaled Features'