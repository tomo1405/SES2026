from src_0776 import task_func


def test_task_func_no_hyphen():
    input_string = "abcde"
    expected_output = {letter: (1 if letter in input_string else 0) for letter in ascii_lowercase}
    assert task_func(input_string) == expected_output

def test_task_func_with_hyphen():
    input_string = "abcde-f"
    expected_output = {letter: (1 if letter in "abcde" else 0) for letter in ascii_lowercase}
    assert task_func(input_string) == expected_output

def test_task_func_empty_string():
    input_string = ""
    expected_output = {letter: 0 for letter in ascii_lowercase}
    assert task_func(input_string) == expected_output

def test_task_func_non_alpha_string():
    input_string = "abc123-!"
    expected_output = {letter: 0 for letter in ascii_lowercase}
    assert task_func(input_string) == expected_output

def test_task_func_single_letter():
    input_string = "a-b"
    expected_output = {letter: (1 if letter == 'a' else 0) for letter in ascii_lowercase}
    assert task_func(input_string) == expected_output

def test_task_func_all_letters():
    input_string = "abcdefghijklmnopqrstuvwxyz"
    expected_output = {letter: 1 for letter in ascii_lowercase}
    assert task_func(input_string) == expected_output

def test_task_func_repeated_letters():
    input_string = "aabbcc-dd"
    expected_output = {letter: (2 if letter in "abc" else 0) for letter in ascii_lowercase}
    assert task_func(input_string) == expected_output