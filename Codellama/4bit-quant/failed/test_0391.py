import pytest
from src_0391 import task_func

def test_task_func_valid_input():
    csv_url_dict = {"URL": "https://example.com/data.csv"}
    expected_df = pd.DataFrame({"title": ["A", "B", "C"], "year": [2000, 2001, 2002]})
    expected_df.sort_values(by="title", inplace=True)
    actual_df = task_func(csv_url_dict)
    assert actual_df.equals(expected_df)

def test_task_func_invalid_input():
    csv_url_dict = {"URL": "https://example.com/data.csv"}
    with pytest.raises(ValueError):
        task_func(csv_url_dict, sort_by_column="invalid_column")