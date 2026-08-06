import pytest
from src_0188 import task_func
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def test_task_func_default_parameters():
    gdf = task_func()
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 5
    assert all(isinstance(coord, Point) for coord in gdf['Coordinates'])

def test_task_func_custom_bounds():
    custom_dic = {'Lon': (0, 10), 'Lat': (0, 10)}
    gdf = task_func(custom_dic)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 5
    assert all(0 <= coord.x <= 10 and 0 <= coord.y <= 10 for coord in gdf['Coordinates'])

def test_task_func_custom_cities():
    custom_cities = ['Paris', 'Berlin', 'Rome']
    gdf = task_func(cities=custom_cities)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 3
    assert all(city in gdf['City'] for city in custom_cities)

def test_task_func_invalid_dic():
    invalid_dic = {'Lon': (0, 10), 'Lat': 0}
    with pytest.raises(ValueError):
        task_func(invalid_dic)

def test_task_func_missing_keys():
    missing_dic = {'Lon': (0, 10)}
    with pytest.raises(ValueError):
        task_func(missing_dic)

def test_task_func_non_tuple_values():
    non_tuple_dic = {'Lon': [0, 10], 'Lat': (0, 10)}
    with pytest.raises(ValueError):
        task_func(non_tuple_dic)