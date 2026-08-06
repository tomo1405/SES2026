import pytest
from src_0990 import task_func

def test_task_func_with_valid_length_and_predicates():
    length = 10
    predicates = ["has_uppercase", "has_lowercase"]
    result_string, results = task_func(length, predicates)
    assert len(result_string) == length
    assert all(results.values())

def test_task_func_with_no_predicates():
    length = 5
    predicates = []
    result_string, results = task_func(length, predicates)
    assert len(result_string) == length
    assert results == {}

def test_task_func_with_all_predicates():
    length = 20
    predicates = ["has_uppercase", "has_lowercase", "has_special_chars", "has_numbers"]
    result_string, results = task_func(length, predicates)
    assert len(result_string) == length
    assert all(results.values())

def test_task_func_with_invalid_predicate():
    length = 10
    predicates = ["has_uppercase", "invalid_predicate"]
    with pytest.raises(KeyError):
        task_func(length, predicates)

def test_task_func_with_negative_length():
    length = -5
    predicates = ["has_uppercase"]
    with pytest.raises(ValueError):
        task_func(length, predicates)

def test_task_func_with_seed():
    length = 10
    predicates = ["has_uppercase", "has_lowercase"]
    seed = 42
    result_string_1, _ = task_func(length, predicates, seed)
    result_string_2, _ = task_func(length, predicates, seed)
    assert result_string_1 == result_string_2

def test_task_func_with_empty_predicates():
    length = 10
    predicates = []
    result_string, results = task_func(length, predicates)
    assert len(result_string) == length
    assert results == {}