import pytest
from src_1081 import task_func

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}

def test_task_func():
    area_string = "2,000"
    price_predicted = task_func(area_string, data=DATA)
    assert price_predicted == 200

def test_task_func_with_new_data():
    area_string = "6,000"
    new_data = {
        "Area_String": ["6,000", "7,000", "8,000", "9,000", "10,000"],
        "Price": [600, 700, 800, 900, 1000],
    }
    price_predicted = task_func(area_string, data=new_data)
    assert price_predicted == 600

def test_task_func_with_invalid_area_string():
    area_string = "invalid"
    with pytest.raises(ValueError):
        task_func(area_string, data=DATA)