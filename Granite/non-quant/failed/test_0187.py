import pytest
from src_0187 import task_func

def test_task_func():
    # Test case 1: Input dictionary is empty
    with pytest.raises(ValueError) as excinfo:
        task_func({})
    assert "Input dictionary is empty." in str(excinfo.value)

    # Test case 2: Input dictionary is not empty
    input_dict = {
        "Location 1": {"Lat": 1, "Lon": 2},
        "Location 2": {"Lat": 3, "Lon": 4},
        "Location 3": {"Lat": 5, "Lon": 6}
    }
    expected_output = (<folium.folium.Map object at 0x7f8e1d1d0c10>, {'Location 1': {'Location 2': 2789.581444553131, 'Location 3': 4865.111015203034}})
    actual_output = task_func(input_dict)
    assert actual_output == expected_output