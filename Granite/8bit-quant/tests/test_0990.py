import pytest
from src_0990 import task_func

def test_task_func():
    length = 10
    predicates = ["has_uppercase", "has_lowercase"]
    seed = 42
    generated_string, results = task_func(length, predicates, seed)
    assert len(generated_string) == length
    assert results["has_uppercase"]
    assert results["has_lowercase"]
    assert not results["has_special_chars"]
    assert not results["has_numbers"]

def test_task_func_invalid_length():
    with pytest.raises(ValueError):
        task_func(-1, ["has_uppercase", "has_lowercase"])

def test_task_func_invalid_predicate():
    with pytest.raises(KeyError):
        task_func(10, ["has_uppercase", "invalid_predicate"])