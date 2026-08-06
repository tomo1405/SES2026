import json
import random
import datetime
from src_0259 import task_func

def test_task_func():
    utc_datetime = datetime.datetime.utcnow()
    seed = 0
    random.seed(seed)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime.isoformat()
    person_json_str = json.dumps(person)
    assert task_func(utc_datetime, seed) == person_json_str

def test_task_func_with_seed_1():
    utc_datetime = datetime.datetime.utcnow()
    seed = 1
    random.seed(seed)
    person = random.choice(DATA)
    person['timestamp'] = utc_datetime.isoformat()
    person_json_str = json.dumps(person)
    assert task_func(utc_datetime, seed) == person_json_str

def test_task_func_with_invalid_seed():
    with pytest.raises(ValueError):
        task_func(datetime.datetime.utcnow(), 'invalid_seed')