import pytest
from src_0187 import task_func
from geopy.distance import geodesic
import folium

def test_task_func_with_empty_dict():
    with pytest.raises(ValueError) as excinfo:
        task_func({})
    assert str(excinfo.value) == "Input dictionary is empty."

def test_task_func_with_single_location():
    input_data = {
        'Location1': {'Lat': 40.7128, 'Lon': -74.0060}
    }
    folium_map, distances = task_func(input_data)
    assert isinstance(folium_map, folium.Map)
    assert distances == {}

def test_task_func_with_two_locations():
    input_data = {
        'Location1': {'Lat': 40.7128, 'Lon': -74.0060},
        'Location2': {'Lat': 34.0522, 'Lon': -118.2437}
    }
    folium_map, distances = task_func(input_data)
    assert isinstance(folium_map, folium.Map)
    expected_distance = geodesic((40.7128, -74.0060), (34.0522, -118.2437)).kilometers
    assert distances == {('Location1', 'Location2'): expected_distance}

def test_task_func_with_three_locations():
    input_data = {
        'Location1': {'Lat': 40.7128, 'Lon': -74.0060},
        'Location2': {'Lat': 34.0522, 'Lon': -118.2437},
        'Location3': {'Lat': 51.5074, 'Lon': -0.1278}
    }
    folium_map, distances = task_func(input_data)
    assert isinstance(folium_map, folium.Map)
    expected_distances = {
        ('Location1', 'Location2'): geodesic((40.7128, -74.0060), (34.0522, -118.2437)).kilometers,
        ('Location1', 'Location3'): geodesic((40.7128, -74.0060), (51.5074, -0.1278)).kilometers,
        ('Location2', 'Location3'): geodesic((34.0522, -118.2437), (51.5074, -0.1278)).kilometers
    }
    assert distances == expected_distances