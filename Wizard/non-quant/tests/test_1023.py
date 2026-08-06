python
import pytest
from src_1023 import task_func

def test_task_func():
    # Test case 1: Valid input
    csv_file_path = "test_data.csv"
    column_name = "date"
    date_format = "%Y-%m-%d"
    expected_output = pd.DataFrame({
        "date": [datetime(2022, 1, 1), datetime(2022, 1, 2), datetime(2022, 1, 3)],
        "value": [1, 2, 3]
    })
    actual_output = task_func(csv_file_path, column_name, date_format)
    assert actual_output.equals(expected_output)

    # Test case 2: Invalid file path
    with pytest.raises(FileNotFoundError):
        task_func("invalid_file.csv", column_name, date_format)

    # Test case 3: Invalid column name
    with pytest.raises(ValueError):
        task_func(csv_file_path, "invalid_column", date_format)

    # Test case 4: Empty dataframe
    csv_file_path = "empty_data.csv"
    with open(csv_file_path, "w") as f:
        f.write("")
    actual_output = task_func(csv_file_path, column_name, date_format)
    assert actual_output.empty