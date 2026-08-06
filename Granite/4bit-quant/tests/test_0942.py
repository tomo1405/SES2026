import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    np.random.seed(random_seed)
    date_range = pd.date_range(start_date, periods=periods, freq=freq)
    sales_forecast = np.random.randint(100, 500, size=periods)
    forecast_df = pd.DataFrame({'Date': date_range, 'Sales': sales_forecast}).set_index('Date')

    fig, ax = plt.subplots()
    forecast_df['Sales'].plot(ax=ax, marker='o')
    ax.set_title('Sales Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.grid(True)
    
    return forecast_df, ax

def test_task_func():
    start_date = '2022-01-01'
    periods = 12
    freq = 'M'
    random_seed = 0
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)
    assert isinstance(forecast_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert forecast_df.index.freq == freq
    assert ax.get_title() == 'Sales Forecast'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'
    assert ax.get_legend() is not None

if __name__ == '__main__':
    pytest.main()