import pytest
from src_0188 import task_func


def test_task_func_valid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    gdf = task_func(dic, cities)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert gdf.shape[0] == len(cities)
    assert gdf.shape[1] == 2
    assert gdf.columns.tolist() == ['City', 'Coordinates']
    assert all(gdf['City'].isin(cities))
    assert all(gdf['Coordinates'].isin(gdf['Coordinates']))

def test_task_func_invalid_input():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    with pytest.raises(ValueError):
        task_func(dic, cities, 'invalid_arg')