import pandas as pd
import numpy as np
import folium
import pytest

from src_0186 import task_func

def test_task_func():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    m, df = task_func(dic, cities)
    assert isinstance(m, folium.folium.Map), "The returned object is not a folium map"
    assert isinstance(df, pd.DataFrame), "The returned object is not a pandas DataFrame"
    assert 'City' in df.columns and 'Longitude' in df.columns and 'Latitude' in df.columns, "The DataFrame does not have the expected columns"
    for _, row in df.iterrows():
        assert row['City'] in cities, "The city in the DataFrame is not in the original list of cities"
        assert row['Longitude'] >= dic['Lon'][0] and row['Longitude'] <= dic['Lon'][1], "The longitude value is not within the expected range"
        assert row['Latitude'] >= dic['Lat'][0] and row['Latitude'] <= dic['Lat'][1], "The latitude value is not within the expected range"

def test_task_func_error():
    dic = {'Lon': (-180, 180), 'Lat': (-90, 90)}
    cities = ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    dic['Lon'] = (180, -180)
    with pytest.raises(ValueError):
        task_func(dic, cities)