import pytest
from src_0942 import task_func

def test_task_func():
    # Test case 1: Check that the function returns a DataFrame and Axes object
    forecast_df, ax = task_func('2022-01-01', 10, 'D')
    assert isinstance(forecast_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Check that the DataFrame has the correct columns and index
    assert set(forecast_df.columns) == {'Date', 'Sales'}
    assert forecast_df.index.name == 'Date'

    # Test case 3: Check that the Axes object has the correct title, xlabel, and ylabel
    assert ax.get_title() == 'Sales Forecast'
    assert ax.get_xlabel() == 'Date'
    assert ax.get_ylabel() == 'Sales'

    # Test case 4: Check that the DataFrame has the correct data
    expected_data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10'],
                     'Sales': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]}
    assert forecast_df.equals(expected_data)

    # Test case 5: Check that the Axes object has the correct grid
    assert ax.grid(True)