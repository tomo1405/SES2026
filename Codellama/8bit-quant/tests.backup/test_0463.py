import pytest
from src_0463 import task_func

def test_task_func_num_rows_negative():
    with pytest.raises(ValueError):
        task_func(num_rows=-1)

def test_task_func_num_rows_zero():
    with pytest.raises(ValueError):
        task_func(num_rows=0)

def test_task_func_num_rows_positive():
    df, ax = task_func(num_rows=100)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(df) == 100
    assert len(ax.get_xticklabels()) == 4
    assert len(ax.get_yticklabels()) == 10

def test_task_func_categories():
    df, ax = task_func(num_rows=100, categories=["a", "b", "c"])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(df) == 100
    assert len(ax.get_xticklabels()) == 3
    assert len(ax.get_yticklabels()) == 10

def test_task_func_random_seed():
    df1, ax1 = task_func(num_rows=100, random_seed=42)
    df2, ax2 = task_func(num_rows=100, random_seed=42)
    assert df1.equals(df2)
    assert ax1.get_figure().equals(ax2.get_figure())