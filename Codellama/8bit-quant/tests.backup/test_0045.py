import pytest
from src_0045 import task_func

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    df, ax = task_func(df)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (5, 2)
    assert ax.get_xlabel() == 'A'
    assert ax.get_ylabel() == 'B'
    assert ax.get_title() == 'Boxplot'
    assert ax.get_xlim() == (0, 1)
    assert ax.get_ylim() == (0, 1)
    assert ax.get_xticks() == [0, 0.25, 0.5, 0.75, 1]
    assert ax.get_yticks() == [0, 0.25, 0.5, 0.75, 1]