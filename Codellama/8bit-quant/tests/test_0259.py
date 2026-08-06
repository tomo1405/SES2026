import json
from datetime import datetime

import pytest
from src_0259 import task_func


def test_task_func_returns_json_string():
    utc_datetime = datetime.datetime.utcnow()
    person_json_str = task_func(utc_datetime)
    assert isinstance(person_json_str, str)
    assert person_json_str.startswith('{')
    assert person_json_str.endswith('}')

def test_task_func_returns_correct_data():
    utc_datetime = datetime.datetime.utcnow()
    person_json_str = task_func(utc_datetime)
    person_data = json.loads(person_json_str)
    assert person_data['name'] in ['John', 'Peter', 'Susan', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
    assert person_data['age'] in range(22, 41)
    assert person_data['city'] in ['New York', 'London', 'Sydney', 'Paris', 'Tokyo', 'Beijing', 'Mumbai', 'Berlin', 'Moscow', 'Rome']
    assert person_data['timestamp'] == utc_datetime.isoformat()

def test_task_func_returns_different_data_with_different_seed():
    utc_datetime = datetime.datetime.utcnow()
    person_json_str_1 = task_func(utc_datetime, seed=0)
    person_json_str_2 = task_func(utc_datetime, seed=1)
    assert person_json_str_1 != person_json_str_2

if __name__ == '__main__':
    pytest.main()