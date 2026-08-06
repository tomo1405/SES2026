import folium
import pandas as pd
import pytest
from src_0186 import task_func


def test_task_func():
    # Test that the function raises a ValueError when the dictionary is missing 'Lon' or 'Lat' keys
    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180)})

    with pytest.raises(ValueError):
        task_func({'Lat': (-90, 90)})

    # Test that the function raises a ValueError when the dictionary values are not tuples
    with pytest.raises(ValueError):
        task_func({'Lon': 180, 'Lat': (-90, 90)})

    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': 90})

    # Test that the function returns a valid map and dataframe when the dictionary is valid
    m, df = task_func({'Lon': (-180, 180), 'Lat': (-90, 90)})
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == len(cities)
    assert 'City' in df.columns
    assert 'Longitude' in df.columns
    assert 'Latitude' in df.columns

    # Test that the function adds markers to the map with the correct coordinates and popup text
    for _, row in df.iterrows():
        assert folium.Marker([row['Latitude'], row['Longitude']], popup=row['City']) in m.markers