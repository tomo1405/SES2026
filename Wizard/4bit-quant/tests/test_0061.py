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
    result = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}]
    task_func(result)

    # Check if CSV file is created
    assert os.path.exists('test.csv')

    # Check if JSON file is created
    assert os.path.exists('test.json')

    # Check if CSV file contains correct data
    with open('test.csv', 'r') as f:
        csv_data = f.read()
        assert csv_data == 'name,age\nJohn,30\nJane,25\n'

    # Check if JSON file contains correct data
    with open('test.json', 'r') as f:
        json_data = json.load(f)
        assert json_data == result

    # Delete CSV and JSON files
    os.remove('test.csv')
    os.remove('test.json')