import json
import random
import datetime
import pytest
from src_0259 import task_func

# Constants
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

# Test case 1: Default behavior
def test_default_behavior():
    utc_datetime = datetime.datetime.now(datetime.timezone.utc)
    random.seed(0)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime.isoformat()
    person_json_str = json.dumps(person)
    assert task_func(utc_datetime) == person_json_str

# Test case 2: Custom seed
def test_custom_seed():
    utc_datetime = datetime.datetime.now(datetime.timezone.utc)
    seed = 12345
    random.seed(seed)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime.isoformat()
    person_json_str = json.dumps(person)
    assert task_func(utc_datetime, seed) == person_json_str

# Test case 3: Invalid input
def test_invalid_input():
    with pytest.raises(TypeError):
        task_func("invalid input")