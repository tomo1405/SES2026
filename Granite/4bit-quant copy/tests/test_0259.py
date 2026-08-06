import json
import random
import datetime
from src_0259 import task_func

DATA = [
    {'name': 'John', 'age': 30, 'city': 'New York'},
    {'name': 'Peter', 'age': 35, 'city': 'London'},
    {'name': 'Susan', 'age': 25, 'city': 'Sydney'},
    {'name': 'Alice', 'age': 28, 'city': 'Paris'},
    {'name': 'Bob', 'age': 40, 'city': 'Tokyo'},
    {'name': 'Charlie', 'age': 22, 'city': 'Beijing'},
    {'name': 'David', 'age': 33, 'city': 'Mumbai'},
    {'name': 'Eve', 'age': 27, 'city': 'Berlin'},
    {'name': 'Frank', 'age': 32, 'city': 'Moscow'},
    {'name': 'Grace', 'age': 29, 'city': 'Rome'}
]

def test_task_func():
    utc_datetime = datetime.datetime(2023, 4, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    seed = 0
    random.seed(seed)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime.isoformat()
    person_json_str = json.dumps(person)
    result = task_func(utc_datetime, seed)
    assert result == person_json_str

def test_task_func_with_different_seed():
    utc_datetime = datetime.datetime(2023, 4, 1, 12, 0, 0, tzinfo=datetime.timezone.utc)
    seed = 1
    random.seed(seed)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime.isoformat()
    person_json_str = json.dumps(person)
    result = task_func(utc_datetime, seed)
    assert result == person_json_str

def test_task_func_with_different_datetime():
    utc_datetime = datetime.datetime(2023, 4, 2, 12, 0, 0, tzinfo=datetime.timezone.utc)
    seed = 0
    random.seed(seed)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime.isoformat()
    person_json_str = json.dumps(person)
    result = task_func(utc_datetime, seed)
    assert result == person_json_str