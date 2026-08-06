import pytest
from src_0391 import task_func

def test_task_func_valid_input():
    csv_url_dict = {"URL": "https://example.com/data.csv"}
    sort_by_column = "title"
    expected_output = pd.DataFrame({"title": ["Title 1", "Title 2", "Title 3"], "author": ["Author 1", "Author 2", "Author 3"]})
    output = task_func(csv_url_dict, sort_by_column)
    assert output.equals(expected_output)

def test_task_func_invalid_input():
    csv_url_dict = {"URL": "https://example.com/data.csv"}
    sort_by_column = "invalid_column"
    with pytest.raises(ValueError):
        task_func(csv_url_dict, sort_by_column)

def test_task_func_invalid_url():
    csv_url_dict = {"URL": "https://example.com/invalid_data.csv"}
    sort_by_column = "title"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(csv_url_dict, sort_by_column)