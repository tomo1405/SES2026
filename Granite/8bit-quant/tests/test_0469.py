import pandas as pd
import numpy as np
import pytest
from src_0469 import task_func

def test_task_func():
    # Test case 1: Default arguments
    df, ax, croot = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(croot, pd.DataFrame)
    
    # Test case 2: Custom arguments
    df, ax, croot = task_func(file_path="custom_data.csv", columns=["X", "Y", "Z"])
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert isinstance(croot, pd.DataFrame)
    
    # Test case 3: Invalid file path
    with pytest.raises(FileNotFoundError):
        df, ax, croot = task_func(file_path="invalid_data.csv")
    
    # Test case 4: Invalid column names
    with pytest.raises(KeyError):
        df, ax, croot = task_func(columns=["D", "E", "F"])