python
import pytest
from src_0187 import task_func

def test_task_func():
    # Test empty dictionary
    with pytest.raises(ValueError):
        task_func({})

    # Test dictionary with one location
    dic = {'A': {'Lat': 1, 'Lon': 2}}
    folium_map, distances = task_func(dic)
    assert len(distances) == 0
    assert isinstance(folium_map, folium.folium.Map)

    # Test dictionary with two locations
    dic = {'A': {'Lat': 1, 'Lon': 2}, 'B': {'Lat': 3, 'Lon': 4}}
    folium_map, distances = task_func(dic)
    assert len(distances) == 1
    assert isinstance(folium_map, folium.folium.Map)
    assert distances[('A', 'B')] == 157.2463164686464

    # Test dictionary with three locations
    dic = {'A': {'Lat': 1, 'Lon': 2}, 'B': {'Lat': 3, 'Lon': 4}, 'C': {'Lat': 5, 'Lon': 6}}
    folium_map, distances = task_func(dic)
    assert len(distances) == 3
    assert isinstance(folium_map, folium.folium.Map)
    assert distances[('A', 'B')] == 157.2463164686464
    assert distances[('A', 'C')] == 150.9929124122762
    assert distances[('B', 'C')] == 150.36231884033203