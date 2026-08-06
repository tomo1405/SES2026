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
    assert task_func('test_input.txt') == [{'a': 1, 'b': {'c': 2}}, {'d': 3, 'e': {'f': 4}}]

    # Test case 2: Invalid input file
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.txt')

    # Test case 3: Empty input file
    with open('empty_file.txt', 'w') as file:
        pass
    with pytest.raises(ValueError):
        task_func('empty_file.txt')

    # Test case 4: Input file with invalid JSON
    with open('invalid_json.txt', 'w') as file:
        file.write('{"a": 1, "b": {"c": 2}, "d": 3, "e": {"f": 4}}')
        file.write('{"g": 5, "h": {"i": 6}, "j": 7, "k": {"l": 8}}')
        file.write('{"m": 9, "n": {"o": 10}, "p": 11, "q": {"r": 12}}')
    with pytest.raises(ValueError):
        task_func('invalid_json.txt')

    # Test case 5: Input file with valid JSON but invalid dictionary format
    with open('invalid_dict.txt', 'w') as file:
        file.write('{"a": 1, "b": {"c": 2}, "d": 3, "e": {"f": 4}}')
        file.write('{"g": 5, "h": {"i": 6}, "j": 7, "k": {"l": 8}}')
        file.write('{"m": 9, "n": {"o": 10}, "p": 11, "q": {"r": 12}}')
        file.write('{"s": 13, "t": {"u": 14}, "v": 15, "w": {"x": 16}}')
    with pytest.raises(ValueError):
        task_func('invalid_dict.txt')

    # Test case 6: Input file with valid JSON and valid dictionary format
    with open('valid_dict.txt', 'w') as file:
        file.write('{"a": 1, "b": {"c": 2}, "d": 3, "e": {"f": 4}}')
        file.write('{"g": 5, "h": {"i": 6}, "j": 7, "k": {"l": 8}}')
        file.write('{"m": 9, "n": {"o": 10}, "p": 11, "q": {"r": 12}}')
        file.write('{"s": 13, "t": {"u": 14}, "v": 15, "w": {"x": 16}}')
    assert task_func('valid_dict.txt') == [{'a': 1, 'b': {'c': 2}}, {'d': 3, 'e': {'f': 4}}, {'g': 5, 'h': {'i': 6}}, {'j': 7, 'k': {'l': 8}}, {'m': 9, 'n': {'o': 10}}, {'p': 11, 'q': {'r': 12}}, {'s': 13, 't': {'u': 14}}, {'v': 15, 'w': {'x': 16}}]