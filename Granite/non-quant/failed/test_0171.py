import pandas as pd
import requests
from io import StringIO
from src_0171 import task_func
import pytest

def test_task_func():
    csv_url = "https://example.com/data.csv"
    response = requests.get(csv_url)
    response.raise_for_status()  # Raise an exception for invalid responses
    csv_data = response.text
    df = pd.read_csv(StringIO(csv_data))
    sorted_df = df.sort_values(by="title")
    expected_result = df.sort_values(by="title")
    actual_result = task_func(csv_url)
    assert actual_result.equals(expected_result)