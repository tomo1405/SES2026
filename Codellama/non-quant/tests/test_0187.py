import folium
import pytest
from src_0187 import task_func


def test_task_func_empty_input():
    with pytest.raises(ValueError):
        task_func({})

def test_task_func_valid_input():
    input_dict = {'location1': {'Lat': 10, 'Lon': 10}, 'location2': {'Lat': 20, 'Lon': 20}}
    folium_map, distances = task_func(input_dict)
    assert isinstance(folium_map, folium.Map)
    assert isinstance(distances, dict)
    assert len(distances) == 1
    assert distances[('location1', 'location2')] == 10