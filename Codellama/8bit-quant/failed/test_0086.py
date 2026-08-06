import pytest
from src_0086 import task_func

def test_task_func():
    start_date = pd.to_datetime("2022-01-01")
    end_date = pd.to_datetime("2022-01-05")
    random_seed = 42

    df, ax = task_func(start_date, end_date, random_seed)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (5, 4)
    assert df.columns.tolist() == ["Date", "Temperature", "Humidity", "Wind Speed"]
    assert df["Date"].dtype == np.datetime64
    assert df["Temperature"].dtype == np.float64
    assert df["Humidity"].dtype == np.float64
    assert df["Wind Speed"].dtype == np.float64
    assert ax.get_title() == "Generated Weather Data"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Temperature, Humidity, Wind Speed"