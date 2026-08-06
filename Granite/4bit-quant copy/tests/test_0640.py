import pytest
from src_0640 import task_func

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.matrix.Axes)
    assert df.shape == (100, 5)
    assert ax.get_xlabel() == 'Feature1'
    assert ax.get_ylabel() == 'Feature2'