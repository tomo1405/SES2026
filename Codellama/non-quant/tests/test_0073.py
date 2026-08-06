import pytest
from src_0073 import task_func

def test_task_func():
    directory = "path/to/directory"
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(hist, np.ndarray)
    assert df.shape[0] > 0
    assert df.shape[1] == 5
    assert hist.shape[0] > 0
    assert hist.shape[1] == 1