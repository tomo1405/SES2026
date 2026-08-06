import pandas as pd
import numpy as np
import pytest
from src_0496 import task_func

def test_task_func():
    # Test with default arguments
    df = task_func(days=10)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 10
    assert "Groceries" in df.columns

    # Test with custom arguments
    df = task_func(days=20, random_seed=42)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 20
    assert "Rent" in df.columns
    assert df["Rent"].iloc[0] == 82

    # Test with invalid arguments
    with pytest.raises(ValueError):
        task_func(days=-1)
    with pytest.raises(TypeError):
        task_func(days="foo")