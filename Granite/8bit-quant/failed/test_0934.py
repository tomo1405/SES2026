import string
import wordninja
from src_0934 import task_func

def test_task_func():
    word = "hello"
    expected_output = [("h", 8), ("e", 5), ("l", 12), ("l", 12), ("o", 15)]
    actual_output, _ = task_func(word)
    assert actual_output == expected_output

def test_task_func_with_punctuation():
    word = "hello, world!"
    expected_output = [("h", 8), ("e", 5), ("l", 12), ("l", 12), ("o", 15), (",", 0), (" ", 0), ("w", 23), ("o", 15), ("r", 18), ("l", 12), ("d", 4), ("!", 0)]
    actual_output, _ = task_func(word)
    assert actual_output == expected_output

def test_task_func_with_numbers():
    word = "12345"
    expected_output = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)]
    actual_output, _ = task_func(word)
    assert actual_output == expected_output

def test_task_func_with_special_characters():
    word = "hello!@#$%^&*()_+"
    expected_output = [("h", 8), ("e", 5), ("l", 12), ("l", 12), ("o", 15), ("!", 0), ("@", 0), ("#", 0), ("$", 0), ("%", 0), ("^", 0), ("&", 0), ("*", 0), ("(", 0), (")", 0), ("_", 0), ("+", 0)]
    actual_output, _ = task_func(word)
    assert actual_output == expected_output

def test_task_func_with_unicode_characters():
    word = "你好，世界"
    expected_output = [("你", 27), ("好", 30), ("，", 0), ("世界", 33)]
    actual_output, _ = task_func(word)
    assert actual_output == expected_output