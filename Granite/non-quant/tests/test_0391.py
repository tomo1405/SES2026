import pandas as pd
import requests
from io import StringIO
from src_0391 import task_func
import pytest

@pytest.mark.parametrize("csv_url_dict, expected_output", [
    ({"URL": "https://example.com/data.csv"}, pd.DataFrame({"column1": [1, 2, 3], "column2": ["a", "b", "c"]})),
    ({"URL": "https://example.com/data2.csv", "sort_by_column": "column2"}, pd.DataFrame({"column1": [3, 2, 1], "column2": ["c", "b", "a"]}))
])
def test_task_func(csv_url_dict, expected_output):
    response_mock = Mock()
    response_mock.text = "column1,column2
1,a
2,b
3,c"
    response_mock.raise_for_status.return_value = None
    requests.get.return_value = response_mock

    actual_output = task_func(csv_url_dict)

    assert actual_output.equals(expected_output)