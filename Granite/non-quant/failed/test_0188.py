import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from src_0188 import task_func
import pytest

def test_task_func_valid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    gdf = task_func(dic, cities)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert 'City' in gdf.columns
    assert 'Coordinates' in gdf.columns
    assert gdf.geometry.name == 'Coordinates'

def test_task_func_invalid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    dic['Lon'] = 'invalid'
    with pytest.raises(ValueError):
        task_func(dic, cities)
    dic['Lon'] = (-180, 180)
    dic['Lat'] = 'invalid'
    with pytest.raises(ValueError):
        task_func(dic, cities)
    dic['Lat'] = (-90, 90)
    cities = 'invalid'
    with pytest.raises(ValueError):
        task_func(dic, cities)