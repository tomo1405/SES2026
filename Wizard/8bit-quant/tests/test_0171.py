python
import pytest
from src_0171 import task_func

def test_task_func():
    csv_url = "https://example.com/data.csv"
    sort_by_column = "title"
    expected_result = pd.DataFrame(
        data=[["title1", "description1"], ["title2", "description2"]],
        columns=["title", "description"],
    )
    result = task_func(csv_url, sort_by_column)
    assert result.equals(expected_result)