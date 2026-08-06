python
import pytest
from src_0186 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func({'Lon': (10, 20), 'Lat': (30, 40)})

    with pytest.raises(ValueError):
        task_func({'Lon': (10, 20), 'Lat': (30, 40), 'Extra': (50, 60)})

    with pytest.raises(ValueError):
        task_func({'Lon': (10, 20), 'Lat': (30, '40')})

    with pytest.raises(ValueError):
        task_func({'Lon': (10, 20), 'Lat': (30, 40), 'Extra': (50, 60)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney', 'Paris'])

    m, df = task_func({'Lon': (-180, 180), 'Lat': (-90, 90)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'])
    assert isinstance(m, folium.Map)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 5
    assert df['City'].tolist() == ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney']
    assert all(df['Longitude'].apply(lambda x: -180 <= x <= 180))
    assert all(df['Latitude'].apply(lambda x: -90 <= x <= 90))