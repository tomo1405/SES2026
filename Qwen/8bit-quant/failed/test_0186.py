import pytest
from src_0186 import task_func
import pandas as pd
import numpy as np
import folium

def test_task_func_default_input():
    m, df = task_func()
    assert isinstance(m, folium.folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(col in df.columns for col in ['City', 'Longitude', 'Latitude'])
    assert all(isinstance(city, str) for city in df['City'])
    assert all(isinstance(lon, float) for lon in df['Longitude'])
    assert all(isinstance(lat, float) for lat in df['Latitude'])

def test_task_func_custom_input():
    custom_dic = {'Lon': (0, 180), 'Lat': (-30, 30)}
    custom_cities = ['Paris', 'Berlin', 'Rome']
    m, df = task_func(custom_dic, custom_cities)
    assert isinstance(m, folium.folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert all(col in df.columns for col in ['City', 'Longitude', 'Latitude'])
    assert all(isinstance(city, str) for city in df['City'])
    assert all(isinstance(lon, float) for lon in df['Longitude'])
    assert all(isinstance(lat, float) for lat in df['Latitude'])
    assert all(lon >= 0 and lon <= 180 for lon in df['Longitude'])
    assert all(lat >= -30 and lat <= 30 for lat in df['Latitude'])

def test_task_func_invalid_dict():
    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180)}, ['New York', 'London'])

def test_task_func_invalid_tuple():
    with pytest.raises(ValueError):
        task_func({'Lon': -180, 'Lat': (-90, 90)}, ['New York', 'London'])

def test_task_func_missing_keys():
    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180)}, ['New York', 'London'])

def test_task_func_non_string_cities():
    with pytest.raises(AssertionError):
        m, df = task_func({'Lon': (-180, 180)}, [123, 'London', 'Beijing'])