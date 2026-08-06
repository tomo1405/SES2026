python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df):
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Date', 'Sales']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Date' and 'Sales' columns.")

    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date')
    resampled_df = df.resample('D').sum()

    if resampled_df.empty or resampled_df['Sales'].sum() == 0:
        raise ValueError("No data available to plot after resampling.")

    ax = resampled_df.plot(y='Sales')
    ax.set_title('Daily Turnover')
    ax.set_ylabel('Sales')
    plt.show()
    return ax

def test_task_func():
    # Test case 1: valid input
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Sales': [100, 200, 300]})
    ax = task_func(df)
    assert isinstance(ax, plt.Axes)

    # Test case 2: invalid input (missing 'Sales' column)
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: invalid input (empty DataFrame)
    df = pd.DataFrame({'Date': [], 'Sales': []})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 4: invalid input (no data after resampling)
    df = pd.DataFrame({'Date': ['2021-01-01', '2021-01-02', '2021-01-03'], 'Sales': [0, 0, 0]})
    with pytest.raises(ValueError):
        task_func(df)