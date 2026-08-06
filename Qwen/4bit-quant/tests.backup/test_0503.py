import pytest
from src_0503 import task_func
from datetime import datetime, timedelta
import pandas as pd
import random

def test_task_func_default():
    ax, df = task_func()
    assert isinstance(ax, sns.axisgrid.FacetGrid), "Return value should be a Seaborn FacetGrid object"
    assert isinstance(df, pd.DataFrame), "Return value should be a Pandas DataFrame"
    assert len(df) == 7 * 5, "DataFrame should have 7 days * 5 activities entries"
    assert all(isinstance(date, datetime.date) for date in df['Date']), "All dates should be datetime.date objects"
    assert all(duration >= 0 and duration <= 120 for duration in df['Duration']), "Durations should be between 0 and 120"

def test_task_func_custom_days():
    ax, df = task_func(days_in_past=3)
    assert len(df) == 3 * 5, "DataFrame should have 3 days * 5 activities entries"

def test_task_func_random_seed():
    ax1, df1 = task_func(random_seed=42)
    ax2, df2 = task_func(random_seed=42)
    assert df1.equals(df2), "DataFrames should be equal with the same random seed"

def test_task_func_invalid_days():
    with pytest.raises(ValueError, match="days_in_past must be in the past"):
        task_func(days_in_past=-1)