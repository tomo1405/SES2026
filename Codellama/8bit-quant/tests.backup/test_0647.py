import pytest
from src_0647 import task_func

def test_task_func():
    csv_path = 'test_data.csv'
    date_column = 'date'

    # Test that the function raises a FileNotFoundError if the file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(csv_path, date_column)

    # Test that the function returns a histogram of the year column
    df = pd.DataFrame({'date': ['2020-01-01', '2020-01-02', '2020-01-03']})
    df[date_column] = df[date_column].apply(lambda x: parse(x))
    expected_hist = df[date_column].dt.year.hist()

    assert task_func(csv_path, date_column) == expected_hist