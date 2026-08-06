import pandas as pd
import numpy as np
import folium
import pytest
from src_0186 import task_func

def test_task_func_valid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    m, df = task_func(dic, cities)
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)

def test_task_func_invalid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    dic['Lon'] = 'invalid'
    with pytest.raises(ValueError):
        task_func(dic, cities)

def test_task_func_missing_key():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    del dic['Lon']
    with pytest.raises(ValueError):
        task_func(dic, cities)

def test_task_func_wrong_type():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    dic['Lon'] = (1, 2, 3)
    with pytest.raises(ValueError):
        task_func(dic, cities)