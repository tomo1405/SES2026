python
import random
import datetime
import pandas as pd
import seaborn as sns
from datetime import timedelta

from src_0503 import task_func

def test_task_func():
    # Test with default arguments
    ax, df = task_func()
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (7, 3)
    assert df.columns.tolist() == ["Date", "Activity", "Duration"]
    assert df["Date"].dtype == "datetime64[ns]"
    assert df["Duration"].dtype == "int64"
    assert df["Activity"].dtype == "object"
    assert ax.data.shape == (7, 3)
    assert ax.data.columns.tolist() == ["Date", "Activity", "Duration"]
    assert ax.data["Date"].dtype == "datetime64[ns]"
    assert ax.data["Duration"].dtype == "int64"
    assert ax.data["Activity"].dtype == "object"

    # Test with custom arguments
    random.seed(0)
    ax, df = task_func(days_in_past=30, random_seed=0)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (30, 3)
    assert df.columns.tolist() == ["Date", "Activity", "Duration"]
    assert df["Date"].dtype == "datetime64[ns]"
    assert df["Duration"].dtype == "int64"
    assert df["Activity"].dtype == "object"
    assert ax.data.shape == (30, 3)
    assert ax.data.columns.tolist() == ["Date", "Activity", "Duration"]
    assert ax.data["Date"].dtype == "datetime64[ns]"
    assert ax.data["Duration"].dtype == "int64"
    assert ax.data["Activity"].dtype == "object"

    # Test with invalid arguments
    try:
        task_func(days_in_past=-1)
    except ValueError as e:
        assert str(e) == "days_in_past must be in the past"