python
import pytest
from src_0187 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func({})

    dic = {'A': {'Lat': 10, 'Lon': 20}, 'B': {'Lat': 30, 'Lon': 40}, 'C': {'Lat': 50, 'Lon': 60}}
    folium_map, distances = task_func(dic)

    assert isinstance(folium_map, folium.Map)
    assert len(distances) == 3
    assert distances[('A', 'B')] == 107.24621155149146
    assert distances[('A', 'C')] == 156.5554613067171
    assert distances[('B', 'C')] == 171.0107577417761