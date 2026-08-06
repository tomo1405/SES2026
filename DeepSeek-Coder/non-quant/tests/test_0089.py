import pytest
from src_0089 import task_func
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

def test_task_func():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    result = task_func(start_date=start_date, end_date=end_date)
    
    assert isinstance(result, tuple), "The function should return a tuple."
    df, ax = result
    assert isinstance(df, pd.DataFrame), "The result should be a DataFrame."
    assert isinstance(ax, plt.Axes), "The plot should be an Axes object."
    assert len(df) > 0, "The DataFrame should not be empty."