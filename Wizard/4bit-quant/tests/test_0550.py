python
import base64
import pandas as pd
import pytest

def task_func(df):
    df = pd.DataFrame(df)
    csv = df.to_csv(index=False)
    csv_bytes = csv.encode('utf-8')
    base64_bytes = base64.b64encode(csv_bytes)
    base64_string = base64_bytes.decode('utf-8')

    return base64_string

def test_task_func():
    df = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
    expected_result = 'U2VsZGVyIHlvdXIgZGVzY3JpcHRpb24='
    assert task_func(df) == expected_result