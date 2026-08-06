import pytest
from src_0785 import task_func

def test_task_func():
    # Test that the function returns a pandas DataFrame
    df = task_func(n=10)
    assert isinstance(df, pd.DataFrame)

    # Test that the DataFrame has the correct columns
    expected_columns = ['Site', 'Category', 'Response', 'Value']
    assert list(df.columns) == expected_columns

    # Test that the DataFrame has the correct number of rows
    assert len(df) == 10

    # Test that the DataFrame contains the correct data
    expected_data = [
        {'Site': 'New York Times', 'Category': 'Sports', 'Response': 'Strongly Disagree', 'Value': 1},
        {'Site': 'USA Today', 'Category': 'Technology', 'Response': 'Disagree', 'Value': 2},
        {'Site': 'Apple News', 'Category': 'Business', 'Response': 'Neither Agree nor Disagree', 'Value': 3},
        {'Site': 'CNN', 'Category': 'Politics', 'Response': 'Agree', 'Value': 4},
        {'Site': 'BBC', 'Category': 'Entertainment', 'Response': 'Strongly Agree', 'Value': 5}
    ]
    assert df.to_dict(orient='records') == expected_data