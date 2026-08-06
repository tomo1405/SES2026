import pytest
from src_1034 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, np.ndarray)
    assert df.shape == (26**3, 3)
    assert list(df.columns) == ["a", "b", "c"]
    assert df["a"].value_counts().index.tolist() == list(string.ascii_lowercase)