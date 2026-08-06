import pytest
from src_0189 import task_func

def test_task_func_valid_input():
    # Test with valid input
    input_dict = {'location1': {'Lat': 37.7749, 'Lon': -122.4194}, 'location2': {'Lat': 37.7949, 'Lon': -122.4294}}
    expected_output = folium.Map(location=[37.7749, -122.4194], zoom_start=4)
    expected_output.add_child(folium.Marker([37.7749, -122.4194], popup='location1'))
    expected_output.add_child(folium.Marker([37.7949, -122.4294], popup='location2'))

    assert task_func(input_dict) == expected_output

def test_task_func_invalid_input():
    # Test with invalid input
    input_dict = {'location1': {'Lat': 37.7749, 'Lon': -122.4194}, 'location2': {'Lat': 37.7949, 'Lon': -122.4294}, 'location3': 'invalid'}
    with pytest.raises(ValueError):
        task_func(input_dict)