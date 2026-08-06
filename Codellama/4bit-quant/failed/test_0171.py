import pytest
from src_0171 import task_func

def test_task_func():
    csv_url = "https://example.com/data.csv"
    sort_by_column = "title"
    response = requests.get(csv_url)
    response.raise_for_status()
    csv_data = response.text
    df = pd.read_csv(StringIO(csv_data))
    sorted_df = df.sort_values(by=sort_by_column)
    assert sorted_df.equals(task_func(csv_url, sort_by_column))