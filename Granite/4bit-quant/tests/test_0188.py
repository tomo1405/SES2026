import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from src_0188 import task_func

def test_task_func_valid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    gdf = task_func(dic, cities)
    assert isinstance(gdf, gpd.GeoDataFrame)

def test_task_func_invalid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    gdf = task_func(dic, cities)
    assert 'City' in gdf.columns and 'Coordinates' in gdf.columns

def test_task_func_lon_not_in_dic():
    dic = {'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    try:
        task_func(dic, cities)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"

def test_task_func_lat_not_in_dic():
    dic = {'Lon': (-180, 180)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    try:
        task_func(dic, cities)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"

def test_task_func_lon_not_tuple():
    dic = {'Lon': -180, 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    try:
        task_func(dic, cities)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"

def test_task_func_lat_not_tuple():
    dic = {'Lon': (-180, 180), 'Lat': -90}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    try:
        task_func(dic, cities)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError not raised"