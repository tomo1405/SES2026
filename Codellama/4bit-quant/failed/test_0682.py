import pytest
from src_0682 import task_func

def test_task_func():
    file_path = 'test_data.json'
    key = 'key'
    df = task_func(file_path, key)
    assert df.shape[0] == 10
    assert df.shape[1] == 2
    assert df.columns.tolist() == ['name', 'age']
    assert df.dtypes.tolist() == ['object', 'int64']
    assert df.index.tolist() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert df.to_json(orient='records') == '[{"name": "John", "age": 25}, {"name": "Jane", "age": 30}, {"name": "Jim", "age": 35}, {"name": "Jake", "age": 40}, {"name": "Jessie", "age": 45}, {"name": "Jimmy", "age": 50}, {"name": "Jenny", "age": 55}, {"name": "Jon", "age": 60}, {"name": "Jimbo", "age": 65}, {"name": "Jimmy", "age": 70}]'