import pandas as pd
import numpy as np
import folium
import pytest

from src_0186 import task_func

@pytest.mark.parametrize("dic, cities, expected_output", [
    ({'Lon': (-180, 180), 'Lat': (-90, 90)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'], (m, df)),
    ({'Lon': (0, 360), 'Lat': (-90, 90)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'], (m, df)),
    ({'Lon': (-180, 180), 'Lat': (-180, 180)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'], (m, df)),
    ({'Lon': (0, 360), 'Lat': (-180, 180)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'], (m, df)),
    ({'Lon': (-180, 180), 'Lat': (0, 360)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'], (m, df)),
    ({'Lon': (0, 360), 'Lat': (0, 360)}, ['New York', 'London', 'Beijing', 'Tokyo', 'Sydney'], (m, df)),
])
def test_task_func(dic, cities, expected_output):
    m, df = task_func(dic, cities)
    assert (m, df) == expected_output