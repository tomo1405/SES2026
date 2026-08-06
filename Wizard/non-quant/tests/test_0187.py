python
import pytest
from src_0187 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func({})

    dic = {'A': {'Lat': 37.7749, 'Lon': -122.4194},
           'B': {'Lat': 37.7750, 'Lon': -122.4195},
           'C': {'Lat': 37.7751, 'Lon': -122.4196}}

    folium_map, distances = task_func(dic)

    assert isinstance(folium_map, folium.folium.Map)
    assert len(distances) == 3
    assert distances[('A', 'B')] == 0.0002
    assert distances[('A', 'C')] == 0.0003
    assert distances[('B', 'C')] == 0.0002