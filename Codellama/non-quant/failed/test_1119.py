import pytest
from src_1119 import task_func

def test_task_func():
    csv_url = 'https://example.com/data.csv'
    json_file_path = 'data.json'
    response = requests.get(csv_url)
    csv_data = csv.reader(StringIO(response.text))

    headers = next(csv_data)
    json_data = [dict(zip(headers, row)) for row in csv_data]

    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file)

    assert task_func(csv_url, json_file_path) == json_file_path