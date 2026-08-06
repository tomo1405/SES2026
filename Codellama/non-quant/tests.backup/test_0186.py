import pytest
from src_0186 import task_func

def test_task_func_valid_input():
    m, df = task_func()
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert all(df['City'].isin(['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']))
    assert all(df['Longitude'].between(-180, 180))
    assert all(df['Latitude'].between(-90, 90))

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90), 'Invalid': 'Invalid'})

def test_task_func_invalid_lon_input():
    with pytest.raises(ValueError):
        task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90), 'Invalid': 'Invalid'})

def test_task_func_invalid_lat_input():
    with pytest.raises(ValueError):
        task_func(dic={'Lon': (-180, 180), 'Lat': (-90, 90), 'Invalid': 'Invalid'})

def test_task_func_invalid_cities_input():
    with pytest.raises(ValueError):
        task_func(cities=['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Invalid'])