import random
import string

import pytest
from src_0990 import task_func


def test_task_func_length_negative():
    with pytest.raises(ValueError):
        task_func(-1, ["has_uppercase"])

def test_task_func_predicates_invalid():
    with pytest.raises(KeyError):
        task_func(10, ["invalid_predicate"])

def test_task_func_seed_none():
    generated_string, results = task_func(10, ["has_uppercase"])
    assert generated_string == "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
    assert results == {"has_uppercase": any(c.isupper() for c in generated_string)}

def test_task_func_seed_not_none():
    generated_string, results = task_func(10, ["has_uppercase"], seed=1234)
    assert generated_string == "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10))
    assert results == {"has_uppercase": any(c.isupper() for c in generated_string)}