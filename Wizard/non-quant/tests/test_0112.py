python
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
    # Test case 1: valid input
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                       'Time': ['00:00:00', '00:00:00', '00:00:00'],
                       'Temperature': [20, 21, 22]})
    ax = task_func(df)
    assert isinstance(ax, sns.axisgrid.axes_grid.AxesGrid)

    # Test case 2: invalid input (missing column)
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                       'Time': ['00:00:00', '00:00:00', '00:00:00'],
                       'Temperature': [20, 21, 22],
                       'Humidity': [50, 51, 52]})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: invalid input (invalid column type)
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                       'Time': ['00:00:00', '00:00:00', '00:00:00'],
                       'Temperature': [20, 21, '22']})
    with pytest.raises(ValueError):
        task_func(df)