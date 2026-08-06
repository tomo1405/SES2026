import pytest
import numpy as np
import pandas as pd
from src_0976 import task_func

def test_task_func():
    # Test with default arguments
    df = task_func(10)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (10, 5)
    assert set(df.columns) == set(["A", "B", "C", "D", "E"])

    # Test with custom arguments
    df = task_func(5, columns=["X", "Y", "Z"], seed=42)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 3)
    assert set(df.columns) == set(["X", "Y", "Z"])
    assert df.loc[0, "X"] == 0.3745401188470954