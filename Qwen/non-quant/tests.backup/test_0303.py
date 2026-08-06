import pytest
from src_0303 import task_func
import pandas as pd

def test_task_func_invalid_input():
    # Test with None input
    with pytest.raises(ValueError):
        task_func(None)

    # Test with empty DataFrame
    df_empty = pd.DataFrame(columns=['Date', 'Value'])
    with pytest.raises(ValueError):
        task_func(df_empty)

    # Test with DataFrame missing 'Value' column
    df_missing_value = pd.DataFrame({'Date': ['2020-01-01']})
    with pytest.raises(ValueError):
        task_func(df_missing_value)

    # Test with DataFrame missing 'Date' column
    df_missing_date = pd.DataFrame({'Value': [10]})
    with pytest.raises(ValueError):
        task_func(df_missing_date)

    # Test with non-DataFrame input
    with pytest.raises(ValueError):
        task_func([{'Date': '2020-01-01', 'Value': 10}])

def test_task_func_valid_input_no_plot():
    df = pd.DataFrame({
        'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
        'Value': [10, 20, 30]
    })
    result = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({
        0: [1.0],
        1: [1.0]
    }))

def test_task_func_valid_input_with_plot():
    df = pd.DataFrame({
        'Date': ['2020-01-01', '2020-01-02', '2020-01-03'],
        'Value': [10, 20, 30]
    })
    result, heatmap = task_func(df, plot=True)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame({
        0: [1.0],
        1: [1.0]
    }))
    assert isinstance(heatmap, sns.axisgrid.heatmap)