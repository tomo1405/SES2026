import pytest
from src_1023 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    column_name = "date_column"

    # Test if the function raises a FileNotFoundError if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(csv_file_path, column_name)

    # Test if the function returns an empty DataFrame if the CSV file is empty
    with open(csv_file_path, "w") as f:
        pass
    with pytest.raises(EmptyDataError):
        task_func(csv_file_path, column_name)

    # Test if the function raises a ValueError if the column is not found in the CSV file
    with open(csv_file_path, "w") as f:
        f.write("date_column,value_columnn2023-01-01,100n2022-01-01,200")
    with pytest.raises(ValueError):
        task_func(csv_file_path, "non_existent_column")

    # Test if the function returns the expected DataFrame if all conditions are met
    with open(csv_file_path, "w") as f:
        f.write("date_column,value_columnn2023-01-01,100n2022-01-01,200")
    expected_df = pd.DataFrame({
        "date_column": ["2023-01-01"],
        "value_column": [100]
    })
    actual_df = task_func(csv_file_path, column_name)
    assert actual_df.equals(expected_df)