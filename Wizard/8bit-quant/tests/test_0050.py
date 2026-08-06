python
import pytest
from src_0050 import task_func

def test_task_func():
    # Test case 1: Empty input list
    with pytest.raises(ValueError):
        task_func([])

    # Test case 2: Valid input list
    timestamps = [1622505600, 1622592000, 1622678400]
    df, ax = task_func(timestamps)
    assert df.shape == (3, 2)
    assert ax.shape == (1, 2)
    assert df["Timestamp"].tolist() == timestamps
    assert df["Datetime"].tolist() == [datetime.fromtimestamp(t).strftime(task_func.DATE_FORMAT) for t in timestamps]