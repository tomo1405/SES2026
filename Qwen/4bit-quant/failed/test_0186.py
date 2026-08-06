import pytest
from src_0186 import task_func
import pandas as pd
import numpy as np

def test_task_func_default_values():
    m, df = task_func()
    assert isinstance(m, folium.folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(df.columns == ['City', 'Longitude', 'Latitude'])
    assert all(df['City'].isin(['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']))

def test_task_func_custom_bounds():
    bounds = {'Lon': (-10, 10), 'Lat': (-5, 5)}
    cities = ['Paris', 'Berlin', 'Moscow', 'Istanbul', 'Cairo']
    m, df = task_func(bounds, cities)
    assert isinstance(m, folium.folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(df.columns == ['City', 'Longitude', 'Latitude'])
    assert all(df['City'].isin(cities))

def test_task_func_invalid_bounds():
    with pytest.raises(ValueError):
        task_func({'Lon': (180, -180), 'Lat': (90, -90)})

def test_task_func_missing_keys():
    with pytest.raises(ValueError):
        task_func({'Lon': (180, -180)})

def test_task_func_non_tuple_values():
    with pytest.raises(ValueError):
        task_func({'Lon': 180, 'Lat': 90})