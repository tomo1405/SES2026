import folium
import pytest
from src_0187 import task_func


def test_task_func():
    # Test case 1: Empty dictionary
    with pytest.raises(ValueError):
        task_func({})

    # Test case 2: Dictionary with invalid values
    with pytest.raises(ValueError):
        task_func({'a': {'Lat': 'abc', 'Lon': 'def'}})

    # Test case 3: Dictionary with valid values
    dic = {'a': {'Lat': 10, 'Lon': 20}, 'b': {'Lat': 30, 'Lon': 40}}
    folium_map, distances = task_func(dic)
    assert isinstance(folium_map, folium.Map)
    assert isinstance(distances, dict)
    assert len(distances) == 2
    assert (10, 20) in distances
    assert (30, 40) in distances

    # Test case 4: Dictionary with multiple locations
    dic = {'a': {'Lat': 10, 'Lon': 20}, 'b': {'Lat': 30, 'Lon': 40}, 'c': {'Lat': 50, 'Lon': 60}}
    folium_map, distances = task_func(dic)
    assert isinstance(folium_map, folium.Map)
    assert isinstance(distances, dict)
    assert len(distances) == 3
    assert (10, 20) in distances
    assert (30, 40) in distances
    assert (50, 60) in distances