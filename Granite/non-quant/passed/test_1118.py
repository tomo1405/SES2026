import pytest
from src_1118 import task_func
import collections
import random
import json

@pytest.fixture
def department_data():
    return collections.defaultdict(int)

def test_task_func(department_data):
    assert task_func(department_data) == json.dumps(collections.defaultdict(list))

def test_task_func_with_valid_data(department_data):
    department_data['EMP$$'] = 10
    department_data['MAN$$'] = 5
    assert task_func(department_data) == json.dumps({'EMP$$': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior'], 'MAN$$': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid']})

def test_task_func_with_invalid_data(department_data):
    department_data['InvalidPrefix'] = 10
    assert task_func(department_data) == json.dumps(collections.defaultdict(list))