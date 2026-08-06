python
import pytest
from src_0391 import task_func

def test_task_func_valid_input():
    csv_url_dict = {"URL": "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv"}
    sorted_df = task_func(csv_url_dict)
    assert sorted_df.shape[0] == 244
    assert sorted_df.shape[1] == 7
    assert sorted_df.columns.tolist() == ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func({})

def test_task_func_sort_by_column():
    csv_url_dict = {"URL": "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv"}
    sorted_df = task_func(csv_url_dict, sort_by_column="total_bill")
    assert sorted_df.iloc[0]["total_bill"] == 14.75
    sorted_df = task_func(csv_url_dict, sort_by_column="tip")
    assert sorted_df.iloc[0]["tip"] == 1.75
    sorted_df = task_func(csv_url_dict, sort_by_column="day")
    assert sorted_df.iloc[0]["day"] == 'Sun'
    sorted_df = task_func(csv_url_dict, sort_by_column="time")
    assert sorted_df.iloc[0]["time"] == 'Dinner'
    sorted_df = task_func(csv_url_dict, sort_by_column="size")
    assert sorted_df.iloc[0]["size"] == 2