import string
import wordninja
from src_0934 import task_func

def test_task_func():
    word = "hello"
    expected_output = [("h", 8), ("e", 5), ("l", 12), ("l", 12), ("o", 15)]
    expected_wordninja_output = ["hello"]
    actual_output = task_func(word)
    assert actual_output[0] == expected_output
    assert actual_output[1] == expected_wordninja_output

def test_task_func_with_numbers():
    word = "12345"
    expected_output = [("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5)]
    expected_wordninja_output = ["12345"]
    actual_output = task_func(word)
    assert actual_output[0] == expected_output
    assert actual_output[1] == expected_wordninja_output

def test_task_func_with_punctuation():
    word = "hello, world!"
    expected_output = [("h", 8), ("e", 5), ("l", 12), ("l", 12), ("o", 15), (",", 0), (" ", 0), ("w", 23), ("o", 15), ("r", 18), ("l", 12), ("d", 4), ("!", 0)]
    expected_wordninja_output = ["hello", "world"]
    actual_output = task_func(word)
    assert actual_output[0] == expected_output
    assert actual_output[1] == expected_wordninja_output