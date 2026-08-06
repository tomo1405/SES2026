import pytest
from src_0990 import task_func

def test_task_func_length_negative():
    with pytest.raises(ValueError):
        task_func(-1, ["has_uppercase"])

def test_task_func_predicates_invalid():
    with pytest.raises(KeyError):
        task_func(10, ["invalid_predicate"])

def test_task_func_predicates_empty():
    with pytest.raises(ValueError):
        task_func(10, [])

def test_task_func_predicates_valid():
    generated_string, results = task_func(10, ["has_uppercase", "has_lowercase"])
    assert "has_uppercase" in results and results["has_uppercase"]
    assert "has_lowercase" in results and results["has_lowercase"]

def test_task_func_seed_provided():
    generated_string1, results1 = task_func(10, ["has_uppercase"], seed=123)
    generated_string2, results2 = task_func(10, ["has_uppercase"], seed=123)
    assert generated_string1 == generated_string2
    assert results1 == results2

def test_task_func_seed_not_provided():
    generated_string1, results1 = task_func(10, ["has_uppercase"])
    generated_string2, results2 = task_func(10, ["has_uppercase"])
    assert generated_string1 != generated_string2
    assert results1 != results2