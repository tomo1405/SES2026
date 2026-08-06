import pandas as pd
from sklearn.linear_model import LinearRegression
from src_1081 import task_func

DATA = {
    "Area_String": ["1,000", "2,000", "3,000", "4,000", "5,000"],
    "Price": [100, 200, 300, 400, 500],
}

def test_task_func():
    area_string = "2,000"
    expected_price = 200
    actual_price = task_func(area_string, data=DATA)
    assert actual_price == expected_price, "Unexpected predicted price"

def test_task_func_with_invalid_area_string():
    area_string = "invalid"
    expected_price = None
    actual_price = task_func(area_string, data=DATA)
    assert actual_price == expected_price, "Unexpected predicted price"