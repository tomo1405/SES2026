python
import pytest
from src_0188 import task_func

def test_task_func():
    # Test with valid input
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    gdf = task_func(dic, cities)
    assert isinstance(gdf, gpd.GeoDataFrame)
    assert len(gdf) == len(cities)
    assert all(isinstance(geom, Point) for geom in gdf.geometry)

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func({'Lon': (180, -180), 'Lat': (-90, 90)}, cities)

    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': (90, -90)}, cities)

    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': (-90, 90)}, ['New York', 'London', 'Beijing', 'Tokyo'])