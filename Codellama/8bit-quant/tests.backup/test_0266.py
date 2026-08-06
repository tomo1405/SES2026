import pytest
from src_0266 import task_func

def test_task_func():
    data = {'b': 2, 'c': 3}
    json_file_name = 'data.json'
    json_file_path = task_func(data, json_file_name)

    assert os.path.exists(json_file_path)
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
        assert json_data['data'] == {'a': 1, 'b': 2, 'c': 3}
        assert json_data['freq'] == {'a': 1, 'b': 1, 'c': 1}