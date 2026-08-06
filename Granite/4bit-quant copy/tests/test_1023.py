import pytest
from src_1023 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    column_name = "date_column"
    date_format = "%Y-%m-%d"

    # Test if the function raises a FileNotFoundError if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(csv_file_path, column_name, date_format)

    # Test if the function returns an empty DataFrame if the CSV file is empty
    df = pd.DataFrame()
    with patch("pandas.read_csv", return_value=df):
        result = task_func(csv_file_path, column_name, date_format)
        assert result.empty

    # Test if the function raises a ValueError if the column is not found in the CSV file
    df = pd.DataFrame({"other_column": [1, 2, 3]})
    with patch("pandas.read_csv", return_value=df):
        with pytest.raises(ValueError):
            task_func(csv_file_path, column_name, date_format)

    # Test if the function converts the column to datetime and filters the data based on the current date
    df = pd.DataFrame({"date_column": ["2022-01-01", "2021-12-31", "2021-12-30"]})
    with patch("pandas.read_csv", return_value=df):
        with patch("datetime.datetime") as mock_datetime:
            mock_datetime.now().date.return_value = datetime.strptime("2022-01-01", "%Y-%m-%d").date()
            result = task_func(csv_file_path, column_name, date_format)
            assert (result["date_column"] == ["2022-01-01"]).all()