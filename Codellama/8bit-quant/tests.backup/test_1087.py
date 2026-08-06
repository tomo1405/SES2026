import pytest
from src_1087 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert len(df) == NUM_SAMPLES
    assert all(isinstance(x, str) for x in df["String Field"])
    assert all(isinstance(x, float) for x in df["Float Field"])
    assert all(x.count(".") == 1 for x in df["Float Field"])
    assert all(x.count(",") == 1 for x in df["Float Field"])
    assert all(x.count("-") == 0 for x in df["Float Field"])
    assert all(x.count("+") == 0 for x in df["Float Field"])
    assert all(x.count("e") == 0 for x in df["Float Field"])
    assert all(x.count("E") == 0 for x in df["Float Field"])