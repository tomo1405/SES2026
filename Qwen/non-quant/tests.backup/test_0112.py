import pytest
from src_0112 import task_func
import pandas as pd

def test_task_func_invalid_input():
    # Test with None input
    with pytest.raises(ValueError):
        task_func(None)

    # Test with non-DataFrame input
    with pytest.raises(ValueError):
        task_func("not a dataframe")

    # Test with missing 'Date' column
    df_missing_date = pd.DataFrame({
        'Time': ['01:00', '02:00'],
        'Temperature': [20, 22]
    })
    with pytest.raises(ValueError):
        task_func(df_missing_date)

    # Test with missing 'Time' column
    df_missing_time = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02'],
        'Temperature': [20, 22]
    })
    with pytest.raises(ValueError):
        task_func(df_missing_time)

    # Test with missing 'Temperature' column
    df_missing_temp = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02'],
        'Time': ['01:00', '02:00']
    })
    with pytest.raises(ValueError):
        task_func(df_missing_temp)

def test_task_func_valid_input():
    df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'],
        'Time': ['01:00', '02:00', '01:00', '02:00'],
        'Temperature': [20, 22, 25, 27]
    })

    ax = task_func(df)
    assert isinstance(ax, sns.axisgrid.FacetGrid)
    assert 'Month' in df.columns
    assert 'Day' in df.columns
    assert df['Month'].dtype == 'int64'
    assert df['Day'].dtype == 'int64'

def test_task_func_pivot_correctness():
    df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02'],
        'Time': ['01:00', '02:00', '01:00', '02:00'],
        'Temperature': [20, 22, 25, 27]
    })

    ax = task_func(df)
    df_pivot = df.pivot(index="Month", columns="Day", values="Temperature")
    assert df_pivot.equals(ax.data)