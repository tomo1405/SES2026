import pytest
from src_0990 import task_func

def test_task_func_with_valid_length_and_predicates():
    length = 10
    predicates = ["has_uppercase", "has_lowercase"]
    seed = 42
    generated_string, results = task_func(length, predicates, seed)
    assert len(generated_string) == length
    assert all(results[predicate] for predicate in predicates)

def test_task_func_with_no_predicates():
    length = 5
    predicates = []
    seed = 42
    generated_string, results = task_func(length, predicates, seed)
    assert len(generated_string) == length
    assert results == {}

def test_task_func_with_all_predicates():
    length = 15
    predicates = ["has_uppercase", "has_lowercase", "has_special_chars", "has_numbers"]
    seed = 42
    generated_string, results = task_func(length, predicates, seed)
    assert len(generated_string) == length
    assert all(results[predicate] for predicate in predicates)

def test_task_func_with_invalid_predicate():
    length = 10
    predicates = ["has_uppercase", "invalid_predicate"]
    seed = 42
    with pytest.raises(KeyError):
        task_func(length, predicates, seed)

def test_task_func_with_negative_length():
    length = -1
    predicates = ["has_uppercase"]
    seed = 42
    with pytest.raises(ValueError):
        task_func(length, predicates, seed)

def test_task_func_with_zero_length():
    length = 0
    predicates = ["has_uppercase"]
    seed = 42
    generated_string, results = task_func(length, predicates, seed)
    assert len(generated_string) == length
    assert results == {}

def test_task_func_with_duplicates_in_predicates():
    length = 10
    predicates = ["has_uppercase", "has_uppercase", "has_lowercase"]
    seed = 42
    generated_string, results = task_func(length, predicates, seed)
    assert len(generated_string) == length
    assert all(results[predicate] for predicate in set(predicates))