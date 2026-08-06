import pytest
from src_0990 import task_func

def test_task_func():
    length = 10
    predicates = ["has_uppercase", "has_lowercase", "has_special_chars", "has_numbers"]
    seed = 42
    generated_string, results = task_func(length, predicates, seed)
    assert len(generated_string) == length
    assert all(result is True for result in results.values())

def test_task_func_invalid_length():
    with pytest.raises(ValueError):
        task_func(-1, ["has_uppercase"])

def test_task_func_invalid_predicate():
    with pytest.raises(KeyError):
        task_func(10, ["has_uppercase", "invalid_predicate"])