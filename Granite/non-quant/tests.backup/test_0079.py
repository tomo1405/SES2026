import pytest
from src_0079 import task_func

@pytest.mark.parametrize("request, header, csv_data, expected_filename", [
    (HttpRequest(), ["Name", "Age"], [["Alice", 25], ["Bob", 30]], "data.csv"),
    (HttpRequest(), ["City", "Country"], [["New York", "USA"], ["London", "UK"]], "data.csv"),
])
def test_task_func(request, header, csv_data, expected_filename):
    response = task_func(request, header, csv_data)
    assert response.get("Content-Type") == "text/csv"
    assert response.get("Content-Disposition") == f"attachment; filename={expected_filename}"