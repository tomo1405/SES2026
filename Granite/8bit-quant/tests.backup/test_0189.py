import pandas as pd
import folium
from geopy.geocoders import Photon
from src_0189 import task_func
import pytest

@pytest.fixture
def sample_input():
    return {
        "Location 1": {"Lat": 37.7749, "Lon": -122.4194},
        "Location 2": "San Francisco, CA, USA",
        "Location 3": {"Lat": 40.7128, "Lon": -74.0060},
        "Location 4": "New York, NY, USA"
    }

def test_task_func(sample_input):
    result = task_func(sample_input)
    assert isinstance(result, folium.Map)

def test_preprocess_locations(sample_input):
    preprocessed_locations = []
    for location, value in sample_input.items():
        if isinstance(value, dict) and 'Lat' in value and 'Lon' in value:
            preprocessed_locations.append({'Location': location, 'Lat': value['Lat'], 'Lon': value['Lon']})
        elif isinstance(value, str):
            geocoded_location = Photon(user_agent="geoapiExercises").geocode(value)
            preprocessed_locations.append({'Location': location, 'Lat': geocoded_location.latitude, 'Lon': geocoded_location.longitude})
        else:
            raise ValueError("Location value must be either a dict with 'Lat' and 'Lon' keys or a string.")
    expected_result = pd.DataFrame(preprocessed_locations)
    result = task_func(sample_input)
    assert result.locations_df.equals(expected_result)

def test_folium_map(sample_input):
    result = task_func(sample_input)
    assert isinstance(result.folium_map, folium.Map)

def test_first_row_coordinates(sample_input):
    result = task_func(sample_input)
    assert result.folium_map.location == (result.locations_df.iloc[0]['Lat'], result.locations_df.iloc[0]['Lon'])

def test_add_markers(sample_input):
    result = task_func(sample_input)
    for _, row in result.locations_df.iterrows():
        assert any(m.location == (row['Lat'], row['Lon']) for m in result.folium_map._children['Layer1'])