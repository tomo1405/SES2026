python
import pytest
from src_0086 import task_func

def test_task_func():
    start_date = '2021-01-01'
    end_date = '2021-01-05'
    random_seed = 42
    
    df, ax = task_func(start_date, end_date, random_seed)
    
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes._subplots.AxesSubplot)
    assert df.shape[0] == 5
    assert df.shape[1] == 4
    assert df.columns.tolist() == ['Date', 'Temperature', 'Humidity', 'Wind Speed']
    assert df['Date'].dtype == 'datetime64[ns]'
    assert df['Temperature'].dtype == 'float64'
    assert df['Humidity'].dtype == 'float64'
    assert df['Wind Speed'].dtype == 'float64'
    assert ax.get_title() == 'Generated Weather Data'