python
import pytest
from src_0188 import task_func

def test_task_func():
    # Test valid input
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    gdf = task_func(dic=dic, cities=cities)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == len(cities)
    assert all(isinstance(coord, Point) for coord in gdf['Coordinates'])

    # Test invalid input
    with pytest.raises(ValueError):
        task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90, 0)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'])

    with pytest.raises(ValueError):
        task_func(dic={'Lon': (-180, 180), 'Lat': (-90)}, cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'])

    with pytest.raises(ValueError):
        task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90)}, cities='New York, London, Beijing, Tokyo, Sydney')