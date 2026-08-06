from datetime import datetime

import pandas as pd
import pytest
import seaborn as sns
from src_0503 import task_func


def test_task_func_default():
    ax, df = task_func()
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 7 * 5  # 7 days in past, 5 activities each day
    assert all(isinstance(date, datetime.date) for date in df['Date'])
    assert all(activity in ["Running", "Swimming", "Cycling", "Yoga", "Weight Training"] for activity in df['Activity'])
    assert all(0 <= duration <= 120 for duration in df['Duration'])

def test_task_func_custom_days():
    ax, df = task_func(days_in_past=3)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3 * 5  # 3 days in past, 5 activities each day

def test_task_func_custom_random_seed():
    ax1, df1 = task_func(random_seed=42)
    ax2, df2 = task_func(random_seed=42)
    assert df1.equals(df2)

def test_task_func_invalid_days_in_past():
    with pytest.raises(ValueError):
        task_func(days_in_past=0)

def test_task_func_no_activities():
    ax, df = task_func(days_in_past=7, random_seed=0)
    assert df['Activity'].nunique() == 5  # Ensure all activities are present

def test_task_func_duration_range():
    ax, df = task_func(days_in_past=7, random_seed=0)
    assert df['Duration'].min() >= 0
    assert df['Duration'].max() <= 120