import pandas as pd
import numpy as np
import pytest

def task_func(file_path="data.csv", columns=["A", "B", "C"]):
    df = pd.read_csv(file_path, dtype=float)
    ax = df[columns].plot()
    croot = np.cbrt(df[columns])
    return df, ax, croot

def test_task_func():
    # Test case 1: Default arguments
    df, ax, croot = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, pd.Series)
    assert isinstance(croot, pd.DataFrame)
    
    # Test case 2: Custom arguments
    df, ax, croot = task_func(file_path="custom_data.csv", columns=["X", "Y", "Z"])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, pd.Series)
    assert isinstance(croot, pd.DataFrame)
    
    # Test case 3: Invalid file path
    with pytest.raises(FileNotFoundError):
        df, ax, croot = task_func(file_path="invalid_data.csv")