import pytest
from src_0186 import task_func
import pandas as pd
import numpy as np
import folium

def test_task_func_default_parameters():
    m, df = task_func()
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(isinstance(city, str) for city in df['City'])
    assert all(-180 <= lon <= 180 for lon in df['Longitude'])
    assert all(-90 <= lat <= 90 for lat in df['Latitude'])

def test_task_func_custom_parameters():
    custom_dic = {'Lon': (0, 360), 'Lat': (-45, 45)}
    custom_cities = ['Paris', 'Berlin', 'Rome']
    m, df = task_func(custom_dic, custom_cities)
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert all(isinstance(city, str) for city in df['City'])
    assert all(0 <= lon <= 360 for lon in df['Longitude'])
    assert all(-45 <= lat <= 45 for lat in df['Latitude'])

def test_task_func_invalid_dic_keys():
    invalid_dic = {'Lon': (0, 360)}
    with pytest.raises(ValueError):
        task_func(invalid_dic)

def test_task_func_invalid_dic_values():
    invalid_dic = {'Lon': 0, 'Lat': (-45, 45)}
    with pytest.raises(ValueError):
        task_func(invalid_dic)

def test_task_func_empty_cities_list():
    m, df = task_func(cities=[])
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 0

def test_task_func_single_city():
    m, df = task_func(cities=['Los Angeles'])
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df['City'][0] == 'Los Angeles'
    assert -180 <= df['Longitude'][0] <= 180
    assert -90 <= df['Latitude'][0] <= 90