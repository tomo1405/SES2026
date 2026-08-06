import pytest
from src_0412 import task_func

def test_task_func():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    output_path = "./test_data_output.json"
    expected_output_path = "./expected_data_output.json"

    actual_output_path = task_func(data, output_path)

    assert actual_output_path == expected_output_path
    assert os.path.exists(actual_output_path)
    with open(actual_output_path) as file:
        data_dict = json.load(file)
        assert data_dict == {"a": [1, 2, 3], "b": [4, 5, 6]}