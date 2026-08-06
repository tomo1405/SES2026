import pytest
from src_0188 import task_func
import numpy as np
import geopandas as gpd
from shapely.geometry import Point

def test_task_func_default_input():
    gdf = task_func()
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 5
    assert all(isinstance(coord, Point) for coord in gdf['Coordinates'])

def test_task_func_custom_bounds():
    bounds = {'Lon': (0, 180), 'Lat': (-90, 0)}
    gdf = task_func(bounds, ['Paris', 'Berlin'])
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 2
    assert all(isinstance(coord, Point) for coord in gdf['Coordinates'])

def test_task_func_invalid_bounds():
    with pytest.raises(ValueError):
        task_func({'Lon': [0, 180], 'Lat': (-90, 0)}, ['Paris', 'Berlin'])

def test_task_func_missing_keys():
    with pytest.raises(ValueError):
        task_func({'Lon': (0, 180)}, ['Paris', 'Berlin'])

def test_task_func_non_tuple_values():
    with pytest.raises(ValueError):
        task_func({'Lon': 0, 'Lat': (-90, 0)}, ['Paris', 'Berlin'])

def test_task_func_empty_cities_list():
    gdf = task_func(cities=[])
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 0

def test_task_func_single_city():
    gdf = task_func(cities=['Oslo'])
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == 1
    assert isinstance(gdf['Coordinates'][0], Point)

def test_task_func_random_coordinates_within_bounds():
    bounds = {'Lon': (0, 180), 'Lat': (-90, 0)}
    gdf = task_func(bounds, ['Paris', 'Berlin'])
    for coord in gdf['Coordinates']:
        assert bounds['Lon'][0] <= coord.x <= bounds['Lon'][1]
        assert bounds['Lat'][0] <= coord.y <= bounds['Lat'][1]