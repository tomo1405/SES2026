python
import pytest
from src_0171 import task_func

def test_task_func():
    # Test case 1: Valid CSV URL and valid sort_by_column
    csv_url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv"
    sort_by_column = "total_bill"
    expected_result = pd.read_csv(StringIO(requests.get(csv_url).text)).sort_values(by=sort_by_column)
    actual_result = task_func(csv_url, sort_by_column)
    assert actual_result.equals(expected_result)

    # Test case 2: Invalid CSV URL
    csv_url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv1"
    with pytest.raises(requests.exceptions.HTTPError):
        task_func(csv_url)

    # Test case 3: Invalid sort_by_column
    csv_url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/tips.csv"
    sort_by_column = "total_bill1"
    with pytest.raises(ValueError):
        task_func(csv_url, sort_by_column)