import pytest
from src_0161 import task_func

def test_task_func():
    data = [[1, 2, 3, 4, 5, 6, 7, 8]]
    df, ax, p = task_func(data)
    assert df.shape[1] == 8
    assert df.columns.tolist() == COLUMN_NAMES
    assert 'Average' in df.columns
    assert ax.get_xlabel() == 'Average'
    assert ax.get_ylabel() == 'Density'
    assert ax.get_title() == 'Average'
    assert len(df['Average']) >= 20
    assert p is not None