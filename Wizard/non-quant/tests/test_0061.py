python
import json
import pandas as pd
import pytest

def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    # Save to CSV
    df = pd.DataFrame(result)
    df.to_csv(csv_file_path, index=False)

    # Save to JSON
    with open(json_file_path, 'w') as f:
        json.dump(result, f, indent=4)

    return None

def test_task_func():
    # Test case 1: Test with empty result
    result = []
    task_func(result)
    assert True

    # Test case 2: Test with non-empty result
    result = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
    task_func(result)
    assert True