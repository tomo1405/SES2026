import pytest
from src_0073 import task_func

def test_task_func():
    directory = "path/to/directory"
    df, hist = task_func(directory)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(hist, np.ndarray)
    assert len(df.columns) == 5
    assert len(df) > 0
    assert len(hist) > 0