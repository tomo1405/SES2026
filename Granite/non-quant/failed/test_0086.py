import pytest
from src_0086 import task_func

def test_task_func():
    start_date = '2023-01-01'
    end_date = '2023-01-10'
    random_seed = 42
    df, ax = task_func(start_date, end_date, random_seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert len(df) == 10
    assert df.columns.tolist() == ['Date', 'Temperature', 'Humidity', 'Wind Speed']
    assert df['Date'].dt.date.tolist() == ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10']
    assert df['Temperature'].min() >= -10 and df['Temperature'].max() <= 40
    assert df['Humidity'].min() >= 20 and df['Humidity'].max() <= 100
    assert df['Wind Speed'].min() >= 0 and df['Wind Speed'].max() <= 20