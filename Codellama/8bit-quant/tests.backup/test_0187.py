import pytest
from src_0187 import task_func

def test_task_func_empty_dict():
    with pytest.raises(ValueError):
        task_func({})

def test_task_func_valid_dict():
    dic = {'loc1': {'Lat': 10, 'Lon': 20}, 'loc2': {'Lat': 30, 'Lon': 40}}
    folium_map, distances = task_func(dic)
    assert isinstance(folium_map, folium.Map)
    assert isinstance(distances, dict)
    assert len(distances) == 2
    assert (10, 20) in distances
    assert (30, 40) in distances