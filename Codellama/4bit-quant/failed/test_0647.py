import pytest
from src_0647 import task_func

def test_task_func():
    csv_path = 'path/to/data.csv'
    date_column = 'date'

    # Test that the function raises an error if the input file does not exist
    with pytest.raises(FileNotFoundError):
        task_func(csv_path, date_column)

    # Test that the function returns a valid histogram
    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))
    hist = task_func(csv_path, date_column)
    assert isinstance(hist, pd.Series)
    assert hist.index.name == 'year'
    assert hist.name == 'count'