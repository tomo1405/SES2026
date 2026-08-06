import pytest
from src_0266 import task_func

def test_task_func():
    data = {'a': 1, 'b': 2, 'c': 3}
    json_file_name = 'test_data.json'
    json_file_path = task_func(data, json_file_name)
    assert os.path.exists(json_file_path)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        assert json_data['data'] == data
        assert json_data['freq'] == {'1': 1, '2': 1, '3': 1}