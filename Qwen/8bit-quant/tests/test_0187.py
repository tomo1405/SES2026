import pytest
from src_0187 import task_func
from geopy.distance import geodesic
import folium

def test_task_func_empty_dict():
    with pytest.raises(ValueError) as excinfo:
        task_func({})
    assert str(excinfo.value) == "Input dictionary is empty."

def test_task_func_single_location():
    input_data = {
        'Location1': {'Lat': 37.7749, 'Lon': -122.4194}
    }
    folium_map, distances = task_func(input_data)
    assert isinstance(folium_map, folium.Map)
    assert distances == {}

def test_task_func_two_locations():
    input_data = {
        'Location1': {'Lat': 37.7749, 'Lon': -122.4194},
        'Location2': {'Lat': 34.0522, 'Lon': -118.2437}
    }
    folium_map, distances = task_func(input_data)
    assert isinstance(folium_map, folium.Map)
    assert len(distances) == 1
    expected_distance = geodesic((37.7749, -122.4194), (34.0522, -118.2437)).kilometers
    assert abs(distances[('Location1', 'Location2')] - expected_distance) < 0.01

def test_task_func_multiple_locations():
    input_data = {
        'Location1': {'Lat': 37.7749, 'Lon': -122.4194},
        'Location2': {'Lat': 34.0522, 'Lon': -118.2437},
        'Location3': {'Lat': 40.7128, 'Lon': -74.0060}
    }
    folium_map, distances = task_func(input_data)
    assert isinstance(folium_map, folium.Map)
    assert len(distances) == 3
    expected_distances = {
        ('Location1', 'Location2'): geodesic((37.7749, -122.4194), (34.0522, -118.2437)).kilometers,
        ('Location1', 'Location3'): geodesic((37.7749, -122.4194), (40.7128, -74.0060)).kilometers,
        ('Location2', 'Location3'): geodesic((34.0522, -118.2437), (40.7128, -74.0060)).kilometers
    }
    for key, value in expected_distances.items():
        assert abs(distances[key] - value) < 0.01