python
import ast
import re
import pytest

def task_func(text_file: str) -> list:
    with open(text_file, 'r') as file:
        text = file.read()

    # Updated regex pattern to handle nested dictionaries more robustly
    pattern = re.compile(r"\{[^{}]*\{[^{}]*\}[^{}]*\}|\{[^{}]*\}")
    matches = pattern.findall(text)

    results = [ast.literal_eval(match) for match in matches]

    return results

def test_task_func():
    # Test case 1: Valid input file
    with open('test_input.txt', 'w') as file:
        file.write('{"a": 1, "b": {"c": 2, "d": 3}, "e": 4}')
    assert task_func('test_input.txt') == [{'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}]

    # Test case 2: Invalid input file
    with open('test_input.txt', 'w') as file:
        file.write('{"a": 1, "b": {"c": 2, "d": 3}, "e": 4')
    with pytest.raises(SyntaxError):
        task_func('test_input.txt')

    # Test case 3: Empty input file
    with open('test_input.txt', 'w') as file:
        file.write('')
    with pytest.raises(ValueError):
        task_func('test_input.txt')

    # Test case 4: Non-existent input file
    with pytest.raises(FileNotFoundError):
        task_func('non_existent_file.txt')