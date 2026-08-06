python
import pytest
from src_0050 import task_func

def test_task_func():
    timestamps = [1622569600, 1622573200, 1622576800]
    df, ax = task_func(timestamps)
    assert df.shape == (3, 2)
    assert ax.shape == (1, 2)
    assert ax[0][0].get_label() == "Timestamp"
    assert ax[0][1].get_label() == "Datetime"
    assert ax[0][0].get_xlim() == (1622569600, 1622576800)
    assert ax[0][1].get_xlim() == (1622569600, 1622576800)
    assert ax[0][0].get_ylim() == (0, 3)
    assert ax[0][1].get_ylim() == (0, 3)