import pytest
from src_0050 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func([])
    timestamps = [1630626400, 1630626460, 1630626520]
    df, ax = task_func(timestamps)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, tuple)
    assert len(ax) == 2
    assert isinstance(ax[0], list)
    assert isinstance(ax[1], str)