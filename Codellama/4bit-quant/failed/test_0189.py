import pytest
from src_0189 import task_func

def test_task_func():
    # Test with valid coordinates
    dic = {'location1': {'Lat': 37.782558, 'Lon': -122.445336},
           'location2': {'Lat': 37.782558, 'Lon': -122.445336}}
    folium_map = task_func(dic)
    assert isinstance(folium_map, folium.Map)
    assert folium_map.location == [37.782558, -122.445336]
    assert folium_map.zoom_start == 4
    assert len(folium_map.markers) == 2
    assert folium_map.markers[0].location == [37.782558, -122.445336]
    assert folium_map.markers[0].popup == 'location1'
    assert folium_map.markers[1].location == [37.782558, -122.445336]
    assert folium_map.markers[1].popup == 'location2'

    # Test with valid string addresses
    dic = {'location1': '1600 Pennsylvania Ave NW, Washington, D.C.',
           'location2': '1 Infinite Loop, Cupertino, CA'}
    folium_map = task_func(dic)
    assert isinstance(folium_map, folium.Map)
    assert folium_map.location == [37.782558, -122.445336]
    assert folium_map.zoom_start == 4
    assert len(folium_map.markers) == 2
    assert folium_map.markers[0].location == [37.782558, -122.445336]
    assert folium_map.markers[0].popup == 'location1'
    assert folium_map.markers[1].location == [37.782558, -122.445336]
    assert folium_map.markers[1].popup == 'location2'

    # Test with invalid input
    with pytest.raises(ValueError):
        task_func({'location1': {'Lat': 37.782558, 'Lon': -122.445336},
                   'location2': {'Lat': 37.782558, 'Lon': -122.445336},
                   'location3': 'invalid'})