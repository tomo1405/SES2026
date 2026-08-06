import pytest
from src_0361 import task_func

def test_task_func():
    file_location = "path/to/file.xlsx"
    sheet_name = "Sheet1"
    expected_result = {"column1": {"mean": 10, "std": 2}, "column2": {"mean": 20, "std": 3}}
    expected_fig = "instance of matplotlib.figure.Figure"

    result, fig = task_func(file_location, sheet_name)

    assert result == expected_result
    assert type(fig) == str(expected_fig)

if __name__ == "__main__":
    pytest.main()