import pandas as pd
import seaborn as sns
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Date', 'Time', 'Temperature']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns.")

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    df_pivot = df.pivot(index="Month", columns="Day", values="Temperature")
    ax = sns.heatmap(df_pivot)
    ax.set_title('Temperature Heatmap')
    return ax

def test_task_func():
    # Test case 1: Invalid 'df'
    with pytest.raises(ValueError) as exc_info:
        task_func("invalid_df")
    assert "Invalid 'df': must be a DataFrame with 'Date', 'Time', and 'Temperature' columns." in str(exc_info.value)

    # Test case 2: Valid 'df'
    valid_df = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Time': ['08:00', '12:00', '16:00'],
        'Temperature': [25, 28, 22]
    })
    ax = task_func(valid_df)
    assert ax.get_title() == 'Temperature Heatmap'