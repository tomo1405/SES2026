import pytest
from src_0990 import task_func

def test_task_func_with_valid_length_and_predicates():
    length = 10
    predicates = ["has_uppercase", "has_lowercase"]
    seed = 42
    result_string, results = task_func(length, predicates, seed)
    assert len(result_string) == length
    assert all(results[predicate] for predicate in predicates)

def test_task_func_with_no_predicates():
    length = 5
    predicates = []
    seed = 42
    result_string, results = task_func(length, predicates, seed)
    assert len(result_string) == length
    assert results == {}

def test_task_func_with_all_predicates():
    length = 20
    predicates = ["has_uppercase", "has_lowercase", "has_special_chars", "has_numbers"]
    seed = 42
    result_string, results = task_func(length, predicates, seed)
    assert len(result_string) == length
    assert all(results[predicate] for predicate in predicates)

def test_task_func_with_invalid_predicate():
    length = 10
    predicates = ["has_uppercase", "invalid_predicate"]
    seed = 42
    with pytest.raises(KeyError) as excinfo:
        task_func(length, predicates, seed)
    assert "Invalid predicate provided." in str(excinfo.value)

def test_task_func_with_negative_length():
    length = -5
    predicates = ["has_uppercase"]
    seed = 42
    with pytest.raises(ValueError) as excinfo:
        task_func(length, predicates, seed)
    assert "Length must be non-negative." in str(excinfo.value)

def test_task_func_with_no_seed():
    length = 10
    predicates = ["has_uppercase", "has_lowercase"]
    result_string1, _ = task_func(length, predicates)
    result_string2, _ = task_func(length, predicates)
    assert result_string1 != result_string2

def test_task_func_with_same_seed():
    length = 10
    predicates = ["has_uppercase", "has_lowercase"]
    seed = 42
    result_string1, _ = task_func(length, predicates, seed)
    result_string2, _ = task_func(length, predicates, seed)
    assert result_string1 == result_string2