import pytest
from src_0188 import task_func
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def test_task_func_default_parameters():
    gdf = task_func()
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert 'City' in gdf.columns
    assert 'Coordinates' in gdf.columns
    assert len(gdf) == 5
    for coord in gdf['Coordinates']:
        assert isinstance(coord, Point)
        assert -180 <= coord.x <= 180
        assert -90 <= coord.y <= 90

def test_task_func_custom_parameters():
    custom_dic = {'Lon': (0, 180), 'Lat': (-30, 30)}
    custom_cities = ['Paris', 'Berlin', 'Madrid']
    gdf = task_func(custom_dic, custom_cities)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert 'City' in gdf.columns
    assert 'Coordinates' in gdf.columns
    assert len(gdf) == 3
    for coord in gdf['Coordinates']:
        assert isinstance(coord, Point)
        assert 0 <= coord.x <= 180
        assert -30 <= coord.y <= 30

def test_task_func_invalid_dic():
    invalid_dic = {'Lon': [-180, 180], 'Lat': (-90, 90)}
    with pytest.raises(ValueError):
        task_func(invalid_dic)

def test_task_func_missing_keys():
    missing_key_dic = {'Lon': (-180, 180)}
    with pytest.raises(ValueError):
        task_func(missing_key_dic)

def test_task_func_non_tuple_values():
    non_tuple_dic = {'Lon': -180, 'Lat': (-90, 90)}
    with pytest.raises(ValueError):
        task_func(non_tuple_dic)