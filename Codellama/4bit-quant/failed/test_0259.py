import pytest
from src_0259 import task_func

def test_task_func():
    # Test that the function returns a JSON string
    utc_datetime = datetime.datetime.utcnow()
    person_json_str = task_func(utc_datetime)
    assert isinstance(person_json_str, str)
    assert person_json_str.startswith('{')
    assert person_json_str.endswith('}')

    # Test that the function returns a JSON string with the correct keys
    person = json.loads(person_json_str)
    assert 'name' in person
    assert 'age' in person
    assert 'city' in person
    assert 'timestamp' in person

    # Test that the function returns a JSON string with the correct values
    assert person['name'] in ['John', 'Peter', 'Susan', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace']
    assert person['age'] in range(20, 41)
    assert person['city'] in ['New York', 'London', 'Sydney', 'Paris', 'Tokyo', 'Beijing', 'Mumbai', 'Berlin', 'Moscow', 'Rome']
    assert person['timestamp'] == utc_datetime.isoformat()

    # Test that the function returns a JSON string with the correct format
    assert person_json_str == json.dumps(person)

def test_task_func_with_seed():
    # Test that the function returns a JSON string with the correct values when a seed is provided
    utc_datetime = datetime.datetime.utcnow()
    person_json_str = task_func(utc_datetime, seed=1234)
    person = json.loads(person_json_str)
    assert person['name'] == 'John'
    assert person['age'] == 30
    assert person['city'] == 'New York'
    assert person['timestamp'] == utc_datetime.isoformat()

if __name__ == '__main__':
    pytest.main()