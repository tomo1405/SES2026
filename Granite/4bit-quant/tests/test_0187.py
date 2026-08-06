import pytest
from src_0187 import task_func

def test_task_func():
    # Test case 1: Input dictionary is empty
    with pytest.raises(ValueError):
        task_func({})

    # Test case 2: Input dictionary is not empty
    input_dict = {"Location 1": {"Lat": 1, "Lon": 2}, "Location 2": {"Lat": 3, "Lon": 4}}
    expected_output = (<folium.folium.Map object>, {"Location 1": {"Location 2": 2.8284271247461903}})
    output = task_func(input_dict)
    assert output == expected_output