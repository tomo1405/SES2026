python
import pytest
from src_0186 import task_func

def test_task_func():
    # Test valid input
    m, df = task_func({'Lon': (-180, 180), 'Lat': (-90, 90)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'])
    assert isinstance(m, folium.folium.Map)
    assert isinstance(df, pd.core.frame.DataFrame)

    # Test invalid input
    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': (-90, 90, 0)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'])

    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': (-90)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'])

    with pytest.raises(ValueError):
        task_func({'Lon': (-180, 180), 'Lat': (-90, 90)}, 'New York,London,Beijing,Tokyo,Sydney')