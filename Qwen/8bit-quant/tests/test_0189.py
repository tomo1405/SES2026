import pytest
from src_0189 import task_func
import pandas as pd
from geopy.geocoders import Photon
import folium

def test_task_func_with_coordinates():
    input_data = {
        'Location1': {'Lat': 40.7128, 'Lon': -74.0060},
        'Location2': {'Lat': 34.0522, 'Lon': -118.2437}
    }
    result_map = task_func(input_data)
    assert isinstance(result_map, folium.folium.Map)
    assert len(result_map._children) == 2  # 1 map object + 2 markers

def test_task_func_with_addresses():
    input_data = {
        'New York': 'New York, USA',
        'Los Angeles': 'Los Angeles, USA'
    }
    result_map = task_func(input_data)
    assert isinstance(result_map, folium.folium.Map)
    assert len(result_map._children) == 2  # 1 map object + 2 markers

def test_task_func_mixed_input():
    input_data = {
        'Location1': {'Lat': 40.7128, 'Lon': -74.0060},
        'New York': 'New York, USA'
    }
    result_map = task_func(input_data)
    assert isinstance(result_map, folium.folium.Map)
    assert len(result_map._children) == 2  # 1 map object + 2 markers

def test_task_func_invalid_input():
    input_data = {
        'Location1': {'Lat': 40.7128},
        'Location2': 'Los Angeles, USA'
    }
    with pytest.raises(ValueError):
        task_func(input_data)

def test_task_func_empty_input():
    input_data = {}
    with pytest.raises(ValueError):
        task_func(input_data)