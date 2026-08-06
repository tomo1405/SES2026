import ast
import re
from src_1094 import task_func

def test_task_func():
    text_file = "example.txt"
    with open(text_file, "w") as file:
        file.write("{a: 1, b: 2}")
        file.write("{c: {d: 3, e: 4}}")
    results = task_func(text_file)
    expected_results = [
        {"a": 1, "b": 2},
        {"c": {"d": 3, "e": 4}}
    ]
    assert results == expected_results

def test_task_func_with_nested_dictionaries():
    text_file = "example.txt"
    with open(text_file, "w") as file:
        file.write("{a: {b: 1, c: 2}}")
        file.write("{d: {e: {f: 3}, g: 4}}")
    results = task_func(text_file)
    expected_results = [
        {"a": {"b": 1, "c": 2}},
        {"d": {"e": {"f": 3}, "g": 4}}
    ]
    assert results == expected_results

def test_task_func_with_invalid_syntax():
    text_file = "example.txt"
    with open(text_file, "w") as file:
        file.write("{a: 1, b: 2")
    results = task_func(text_file)
    expected_results = []
    assert results == expected_results